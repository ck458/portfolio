# Selected Implementation Samples

Four representative engineering modules from the showcased projects:

- [Workspace boundary checks](novel-engine/workspace_paths.py)
- [Durable atomic I/O](novel-engine/io_utils.py)
- [Paired bootstrap for model evaluation](evaluation/paired_bootstrap.py)
- [Typed date period operations](study-logs/period.ts)

To run the Python regression checks:

~~~bash
python -m pip install -r samples/evaluation/requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
~~~

See [project case studies](../README.md) and [technical details](../docs/code-gallery.md).
