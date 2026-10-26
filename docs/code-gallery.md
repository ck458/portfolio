# Selected Code | 精选工程实现

[首页](../README.md) · [架构](system-architecture.md) · [项目目录](project-index.md)

精选四个具有明确技术侧重点的模块，均可直接阅读。Python 示例提供跨平台自动化测试。

| Module | 工程主题 |
| --- | --- |
| [workspace_paths.py](../samples/novel-engine/workspace_paths.py) | 工作区根目录约束与路径校验 |
| [io_utils.py](../samples/novel-engine/io_utils.py) | 原子文件持久化、flush / fsync / replace |
| [paired_bootstrap.py](../samples/evaluation/paired_bootstrap.py) | 配对样本、准确率变化、置信区间 |
| [period.ts](../samples/study-logs/period.ts) | 时区、自然周月与数据查询周期 |

### Test

~~~bash
python -m pip install -r samples/evaluation/requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
~~~

### Paired evaluation

输入 JSONL 中每行包含 id 和 correct 字段：

~~~bash
python samples/evaluation/paired_bootstrap.py --baseline baseline.jsonl --candidate candidate.jsonl --output report.json
~~~

输出包含 paired_samples、accuracy_delta、答案正确性转移及 bootstrap_ci。

[GitHub Actions](https://github.com/ck458/portfolio/actions/workflows/samples.yml) · [项目证据](engineering-evidence.md)
