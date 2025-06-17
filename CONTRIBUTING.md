# 贡献指南

在你开始贡献之前，请花一些时间阅读以下指南。这有助于确保你——尤其是从未使用 Github 的朋友——的贡献能够顺利地被接受和合并。

## 如何贡献新的文学摘抄

1.  **Fork 本仓库**：
    *   首先，点击本仓库右上角的 `Fork` 按钮，将本仓库派生到你的 GitHub 账户下。

2.  **克隆你的派生仓库**：
    *   将你派生出的仓库克隆到你的本地计算机：
        ```bash
        git clone https://github.com/你的GitHubID/literature-clock-zh.git
        ```
    *   进入项目目录：
        ```bash
        cd literature-clock-zh
        ```

3.  **创建新分支**：
    *   为了更好地管理你的修改，请为你的贡献创建一个新的分支。分支名称应具有描述性，例如 `feat/add-08-30-quotes`：
        ```bash
        git checkout -b feat/add-your-time-quotes
        ```

4.  **添加或修改摘抄数据**：
    *   所有的摘抄数据都存储在 `quotes/` 文件夹下。
    *   找到你想要添加或修改摘抄对应的时间点文件（例如，如果你想为 08:30 添加摘抄，请打开或创建 `quotes/08-30.json` 文件）。
    *   如果文件不存在，请创建一个新的 JSON 文件。
    *   每个 JSON 文件应包含一个 JSON 数组，数组中的每个元素都是一个摘抄对象。

5.  **提交你的修改**：
    *   将你的修改添加到暂存区：
        ```bash
        git add quotes/你的文件.json
        ```
    *   提交你的修改。提交信息应该清晰简洁，描述你所做的更改。建议使用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) 规范，例如 `feat: add new quotes for 08:30` 或 `docs: update contributing guide`：
        ```bash
        git commit -m "feat: 添加 08:30 的新摘抄"
        ```

6.  **推送你的分支**：
    *   将你的新分支推送到你派生出的 GitHub 仓库：
        ```bash
        git push origin feat/add-your-time-quotes
        ```

7.  **创建 Pull Request (PR)**：
    *   在你将分支推送到 GitHub 后，访问你的 GitHub 派生仓库页面。GitHub 会提示你创建一个 `Pull Request`。
    *   点击 `Compare & pull request` 按钮。
    *   在 Pull Request 页面，确保目标分支是本仓库的 `main` 分支。
    *   填写清晰的 Pull Request 标题和描述，解释你所做的更改。
    *   点击 `Create pull request`。

## 规范

对于数据文件的 JSON 格式，请严格遵循上述数据结构。确保 JSON 有效且字段正确。

## 审核流程

在你提交 Pull Request 后，项目维护者会进行审核。我们可能会提出问题、建议修改或要求你解决一些问题。请耐心等待，并及时响应评论。一旦你的贡献被接受，它将被合并到主分支中。