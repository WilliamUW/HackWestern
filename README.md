# ScreenBuddy - Hack Western X, November 24-26, 2023

<!-- BACK TO TOP -->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->

<div align="center">
  <a href="https://github.com/WilliamUW/HackWestern"></a>
 
  [<img src="https://img.youtube.com/vi/MGNQpf0Cvo4/0.jpg" width="700">](https://www.youtube.com/watch?v=MGNQpf0Cvo4)

  <h3 align="center"></h3>
  <p align="center">
    <b style="color: #AADDDF">⬆️View Demo</b>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## Problem:

Before we get started with our pitch, who here has heard of Photoshop? Likely most people given it’s the most popular image editor in the world.

Who here knows how to use every single feature that Photoshop offers? Likely no one, and for a good reason. Any idea how long you think the manual for Photoshop is?

It’s not 50 or 100 or 500 pages. It’s **1017** pages.

![image1](https://github.com/WilliamUW/HackWestern/assets/58105903/542b9374-5221-40f1-a781-8819995e75b5)
Adobe Photoshop - World’s most popular image editor.
https://helpx.adobe.com/pdf/photoshop_reference.pdf


<i>**And this isn’t an isolated case!**</i>


![image3](https://github.com/WilliamUW/HackWestern/assets/58105903/889ca840-285e-4b2e-8a06-684748848ec1)
Adobe Premiere Pro - World’s most popular video editor has a **818** pages manual.
https://helpx.adobe.com/content/dam/help/en/pdf/premiere_pro_reference.pdf

<br />

![image4](https://github.com/WilliamUW/HackWestern/assets/58105903/29a0231f-c482-42ac-ae8e-14315eff3f13)
DaVinci Resolve - World’s most popular free video editor has a **1060** pages manual.
https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_12_Reference_Manual.pdf

As inexperienced video editors who needed to edit a demo video for this hackathon, we thought there has to be a better way to learn and use the features without going through thousand page manuals and hour long YouTube videos.

Why can’t some"buddy" just tell me exactly what to do?

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Solution:

That’s the problem we decided to solve at Hack Western!

Imagine an AI companion that could not only understand your queries but also helps one navigate the user interface in realtime, providing step-by-step guidance through screen sharing while articulating instructions audibly. 

Essentially ChatGPT but it can help you with whatever is on your screen in realtime!

Welcome to the new age of AI collaboration - <b>Share your vision with ScreenBuddy!</b>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Tech Stack:

The tech stack comprises:
- A powerful combination of OpenCV and GPT-4-Vision for robust image recognition capabilities. 
- Vector embeddings are crafted using ChromaDB and LangChain, tailored specifically for training on DaVinci Resolve and Circle documentation, enhancing understanding and context. 
- GPT Whisper handles speech-to-text conversion.
- GPT TTS seamlessly transforms text to speech. 
- The user interface is facilitated by the Tkinter Python Toolkit, offering a user-friendly screen-sharing experience for effective interaction with the AI system. 

This comprehensive stack creates a synergistic environment, enabling intuitive and efficient navigation through complex interfaces, whether in video editing with DaVinci Resolve or managing blockchain transactions on Circle.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Challenges we ran into:

- Integrating OpenCV and GPT-4-Vision for seamless image recognition posed technical hurdles when it came to streaming visual media files.
- Fine-tuning vector embeddings using ChromaDB and LangChain required iterative experimentation to achieve good results with DaVinci Resolve.
- Ensuring real-time responsiveness in Tkinter Python Toolkit for effective screen sharing and speech recognition was a significant challenge.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Accomplishments that we're proud of:

- Successful integration of OpenCV and GPT-4-Vision for robust image recognition capabilities.
- Precision in crafting vector embeddings via ChromaDB and LangChain for tailored training on DaVinci Resolve and Circle documentation.
- Seamless implementation of GPT Whisper and GPT TTS for speech-to-text and text-to-speech transformations.
- Development of a user-friendly interface using Tkinter Python Toolkit for intuitive screen sharing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## What we learned:

- The synergy between computer vision and natural language processing is pivotal for effective AI-assisted navigation.
- The importance of iterative testing and fine-tuning in creating a reliable and user-friendly system.
- Addressing real-time responsiveness challenges in UI interactions enhances overall user experience.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## What's next for our project:

- Implementing user feedback for continuous improvement and refinement.
- Exploring additional applications beyond DaVinci Resolve and Circle for a broader user base.
- Enhancing the AI's contextual understanding for even more intuitive interactions.
- Collaborating with the community to expand the range of supported interfaces and functionalities.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
1. Clone the repo
2. add OPENAI_API_KEY="yourkey" to .env

 ```
pip install sounddevice soundfile numpy playsound pillow opencv-python openai pyautogui
Issues: speech_recognition
python screenshare.py
python main.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
* Andy Huang - <a href="https://github.com/andy0207huang"></a> [![LinkedIn][linkedin-shield-andy]][linkedin-url-andy]
* William Wang - <a href="https://github.com/SurjaHead"></a> [![LinkedIn][linkedin-shield-william]][linkedin-url-william]



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BADGES / SHIELD / IMAGES / URL -->
[OpenCV]: https://img.shields.io/badge/OpenCV-36454F?style=for-the-badge
[Python]: https://img.shields.io/badge/Python-36454F?style=for-the-badge
[GPT-4-Vision]: https://img.shields.io/badge/GPT4Vision-36454F?style=for-the-badge
[Whisper]: https://img.shields.io/badge/Whisper-36454F?style=for-the-badge

[Circle]: https://img.shields.io/badge/Circle-000000?style=for-the-badge
[Infobip]: https://img.shields.io/badge/Infobip-000000?style=for-the-badge
[GoDaddy]: https://img.shields.io/badge/GoDaddy-000000?style=for-the-badge

[linkedin-shield-andy]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0072b1
[linkedin-url-andy]: https://www.linkedin.com/in/andy-snowflake-huang/
[linkedin-shield-william]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0072b1
[linkedin-url-william]: https://www.linkedin.com/in/williamuw/
