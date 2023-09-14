<<<<<<< HEAD
# Voice-Interaction
A speech interaction system based on autoregressive language model
=======
## 基于百度智能云API和Openai-Gpt3.5的语音交互模块



### 实现效果

![image-20230317153824920](C:\Users\DDMonkey\AppData\Roaming\Typora\typora-user-images\image-20230317153824920.png)

​	（仍存在一定的问题。。。例如部分具有时效性的问题，api无法准确的获取信息）

### 技术构建

* **百度智能云API**

  * 语音识别
  * 语音合成

  ![image-20230317152531019](C:\Users\DDMonkey\AppData\Roaming\Typora\typora-user-images\image-20230317152531019.png)

* **Gpt3.5-turbo**

  * 自回归语言模型

    ​	GPT-3.5是**OpenAI的预训练模型**，它内置了大量的参数，可以帮助开发者轻松进行finetuning，从而快速解决NLP任务。 此外，GPT-3.5也支持深度微调，并且它有一个快速可扩展的架构，可以轻易适应多种任务，因此，GPT-3.5可以说是人工智能领域当前最强大的NLP模型之一。

    ![image-20230317152806543](C:\Users\DDMonkey\AppData\Roaming\Typora\typora-user-images\image-20230317152806543.png)

* ***Snowboy（未实现）***

  * 语音唤醒

    ​	一款离线语音唤醒引擎，只能在树莓派或Ubuntu等操作系统上运行。目前已经停止维护，没有新的umdl，但是还可以有pmdl使用。

    ![image-20230317153011657](C:\Users\DDMonkey\AppData\Roaming\Typora\typora-user-images\image-20230317153011657.png)



### 补充说明

* 原打算使用**图灵机器人**的自回归语言模型，但是图灵机器人的认证一直没有通过，而别的语言模型，比如青云客，小i机器人，如意机器人，天行机器人等都不太适合用于语音交互上。最后只能选择openai中的gpt3.5作为本项目的语言模型，本项目中语言模型未做任何训练。
* 本项目仅用于记录，不保证项目的正常运行。
>>>>>>> 50b0c25 (提交文件)
