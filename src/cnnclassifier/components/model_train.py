from pathlib import Path
from cnnclassifier.entity.config_entity import ModelTrainConfig
import os
import urllib.request as request
import tensorflow as tf
import time
from zipfile import ZipFile
tf.config.run_functions_eagerly(True)

import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config):
        self.config = config
        # Ensure eager execution is enabled
        tf.config.run_functions_eagerly(True)

    def get_base_model(self):
        # Load the model without compiling it
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path, compile=False)
        # Compile a fresh optimizer for training
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.02),
            loss='categorical_crossentropy',  # replace with your loss if different
            metrics=['accuracy']
        )

    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,   # fixed: use float division
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation='bilinear'
        )

        # Validation generator
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # Training generator
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )


