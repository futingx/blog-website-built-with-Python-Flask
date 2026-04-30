---
title: "Markdown 写作完全指南"
slug: markdown-guide
date: "2026-04-20"
category: "工具"
tags: ["Markdown", "写作", "工具"]
summary: "Markdown 是一种轻量级标记语言，让写作者能够用简洁的语法编写格式化文本。本文详细介绍 Markdown 的各种语法和使用技巧。"
cover: ""
---

## 什么是 Markdown？

Markdown 由 John Gruber 和 Aaron Swartz 于 2004 年创建，是一种使用纯文本格式编写富文本的轻量级标记语言。它的设计目标是易读易写。

## 基础语法

### 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
```

### 段落与换行

段落之间需要空行。如果需要换行，在行末添加两个空格或使用 `<br>` 标签。

### 强调

```markdown
*斜体* 或 _斜体_
**粗体** 或 __粗体__
***粗斜体***
~~删除线~~
```

渲染效果：*斜体*、**粗体**、***粗斜体***、~~删除线~~

### 列表

无序列表：
```markdown
- 项目一
- 项目二
  - 子项目
  - 子项目
```

有序列表：
```markdown
1. 第一步
2. 第二步
3. 第三步
```

## 进阶语法

### 链接与图片

```markdown
[链接文字](https://example.com)
![图片描述](image-url.jpg)
```

### 引用

```markdown
> 这是一个引用块
> 可以包含多行
```

### 代码块

行内代码：`print("Hello World")`

代码块（指定语言）：
```python
def hello():
    print("Hello, Markdown!")
```

### 表格

```markdown
| 列1 | 列2 | 列3 |
|-----|-----|-----|
| A1  | B1  | C1  |
| A2  | B2  | C2  |
```

### 任务列表

```markdown
- [x] 已完成任务
- [ ] 未完成任务
- [ ] 另一个任务
```

## Markdown 在博客中的应用

在这个博客系统中，文章的元数据通过 YAML front matter 定义：

```yaml
---
title: "文章标题"
date: "2026-04-20"
category: "分类"
tags: ["标签1", "标签2"]
summary: "文章摘要"
---
```

---

掌握 Markdown，让你的写作更高效！
