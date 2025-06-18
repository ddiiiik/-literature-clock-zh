# 文学时钟（中文版摘抄）

本项目灵感来源于 Jaap Meijers 的 [E-reader clock](https://techni.gallery/literaire-klok-trekt-internationaal-aandacht/) 和 Johannes Enevoldsen
的 [literature-clock](https://github.com/JohannesNE/literature-clock?tab=License-1-ov-file) ，致力于收集和展示与时分相关的中文文学摘抄。


---


多年前，我读过一个[送礼故事](https://techni.gallery/literaire-klok-trekt-internationaal-aandacht/) ，印象深刻。

> 我女友好读书。作为一名英语文学教师和学者，她平均每年读 80 本书。
>
> 她的愿望清单上有一个放在客厅的钟。我本可从商店买个挂钟，但那样还有什么意思呢？于是，我给她做了一个钟——用 Kindle 作为显示屏，引用文学作品里的时间指示来报时。
>
> 它每分钟更新一次，例如，晚上 9 点 23 分将显示：
>
> My father met me at the station, the dog jumped up to meet me, missed, and nearly fell in front of the 9.23 pm Birmingham express.

![literary_clock_by_jaap_meijers](/images/literary_clock_by_jaap_meijers.jpg)

令我惊喜的是，作者 Jaap Meijers 不仅提供了自制手册，更将那些与时分一一对应的文学摘抄开源了。

不禁想，何不将这一雅致的创意移植到 [KeyHour（我开发的一个数码时钟 app）](https://apps.apple.com/app/id6467558399) ？实践证明，效果甚佳：

![keyhour_literary_clock](/images/keyhour_literary_clock.jpg)

又不禁想，当前开源摘抄都是英文的，何不引用中文文学作品？比如，17:30 便可引用三毛《结婚记》中的这一段：

> 第二天荷西来敲门时我正在睡午觉，因为来回提了一大桶淡水，累得很。已经五点半了。他进门就大叫：“快起来，我有东西送给你。”口气兴奋得很，手中抱着一个大盒子。

书到用时方恨少。

又又不禁想，何不集众人之力，共同发掘那些散落在中文文学作品里的时间印记？因此，在此诚挚邀请你——若在日常阅读中偶遇带有具体时分的句子，请不吝与我分享。

无以为报，但你的名字将被列入 KeyHour（以及计划开发的文学时钟 Mac 屏保应用） 的摘抄贡献者名单。

摘抄内容不限于中国作者，中文即可（当然，若摘抄出自华语作者更佳）。摘抄可直接提及时间，也可通过意境、场景等与特定时间概念相呼应。

## 摘抄的数据结构

所有摘抄数据均存储于 `quotes/` 文件夹下，以 JSON 文件的形式存在。每个文件代表一个特定的时间点（例如 `00-00.json` 代表 00:00），并且包含一个或多个与该时间点相关的摘抄。

摘抄数据结构示例如下：

```json
[
  {
      "time": "17:30",
      "label": "五点半",
      "quote": "第二天荷西来敲门时我正在睡午觉，因为来回提了一大桶淡水，累得很。已经五点半了。他进门就大叫：\"快起来，我有东西送给你。\"口气兴奋得很，手中抱着一个大盒子。",
      "source": "撒哈拉的故事",
      "author": "三毛",
      "tag": "sfw",
      "collected_by": "东炜黄"
  }
]
```

### 字段说明

*   `time`：时分，格式为 "HH:MM"，例如 "17:30"
*   `label`：该时间点在摘抄中的描述，例如 "五点半"
*   `quote`：具体的中文文学摘抄内容
*   `source`：摘抄的来源文学作品名称（无需书名号）
*   `author`：作者名称（请尽可能填写其全名，例如 "弗朗茨 · 卡夫卡"，而不是 "卡夫卡"）
*   `tag`：用于标记内容特性的标签
    *   `sfw` (Safe For Work)：表示该摘抄内容是"工作安全的"，即不包含任何可能不适宜在公共场合或工作环境中查看的内容（例如：粗俗语言、敏感话题等）
    *   `unknown`：如不确定，可写 unknown
*   `collected_by`：摘抄者名称

## 如何贡献

请在贡献之前仔细阅读 [贡献指南](CONTRIBUTING.md)。