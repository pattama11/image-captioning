# Image captioning

## Description

Image captioning is a technology that automatically generates descriptive textual captions for images using a combination of computer vision and natural language processing techniques. This process involves extracting visual features from the image using deep learning models like Convolutional Neural Networks (CNNs) and then using these features as input to a natural language generation model such as a Recurrent Neural Network (RNN) or Transformer-based model. The output is a human-like description of the image, including details about objects, scenes, actions, and other relevant elements. Image captioning has diverse applications, from aiding visually impaired individuals by providing image descriptions to improving image search engines and enhancing the accessibility of content on social media platforms.

## Team members

401119 Pattama Yodthong

400968 Kanokkrit Kangwankiat

400351 Theethut Narksenee

400139 Kanet Saengming

402978 Takapol Tanthavach

## Introduction

Currently, there is no treatment for the visually impaired. Therefore, technology that will help improve the quality of life of these people is by allowing them to know things around them through sound. To get the sound, we must first know what's happening in the picture, which image captioning can help with in this part.

## Development

In development state, we will focus on zero shot model because it is quite resource-saving than other methods. And it also takes quite a bit of time. (In addition, the team also tried using few-shot.) After getting the results, we had to choose a model whose translated language was not strange or would not change the context of the received text.
After that, we do post processing, which involves manipulating the data before sending. It removes certain patterns from the results that we get, such as tons of special characters. These patterns are not counted as language. It's just something stuck from the model's incorrect prediction, so it must be removed before sending.

## Improvement

It may need to be developed to be more accurate. Because writing the wrong caption can cause misunderstandings and the model must be made small so that it can be used in a mobile phone or headphones that is easy to carry.

