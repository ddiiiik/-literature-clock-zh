# 文学时钟（中文版）

本项目是 Jaap Meijers 的 [E-reader clock](https://techni.gallery/literaire-klok-trekt-internationaal-aandacht/) 和 Johannes Enevoldsen
的 [literature-clock](https://github.com/JohannesNE/literature-clock?tab=License-1-ov-file) 的中文版，致力于收集和展示与时间点相关的中文文学摘抄。

摘抄内容不限于中国作者，中文即可（当然，若摘抄出自华语作者更佳）。摘抄可直接提及时间，也可通过意境、场景等与特定时间概念相呼应。

## 数据结构

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
*   `author`：作者名称（请尽可能填写其全名，例如 "弗朗茨 ·卡夫卡"，而不是 "卡夫卡"）
*   `tag`：用于标记内容特性的标签
    *   `sfw` (Safe For Work)：表示该摘抄内容是"工作安全的"，即不包含任何可能不适宜在公共场合或工作环境中查看的内容（例如：粗俗语言、敏感话题等）
    *   `unknown`：如不确定，可写 unknown（未知）
*   `collected_by`：摘抄者名称

## 如何贡献

请在贡献之前仔细阅读 [贡献指南](CONTRIBUTING.md)。