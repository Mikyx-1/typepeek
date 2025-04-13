# 📦 typepeek

**typepeek** is a lightweight Python package that infers accurate, human-readable type hints from runtime data — including nested and complex containers like lists, dictionaries, tuples, sets, and even third-party objects like PyTorch tensors.

---

## 🚀 Quick Start

### Installation

```bash
pip install typepeek
```

### Example Usage

```python
from typepeek import infer_type
import torch

data = [torch.tensor(1), torch.tensor(2), 3]
print(infer_type(data))
# Output: List[Union[torch.Tensor, int]]
print(infer_type(data, agnostic=False))
#typing.List[torch.Tensor, torch.Tensor, int]
```

---

## ✨ Features

- ✅ **Precise Type Inference** — Accurately infers human-readable type hints from runtime values
- 🔁 **Deep Nested Structure Support** — Handles arbitrarily nested containers (e.g., `List[Dict[str, Tuple[int, float]]]`)
- 🧹 **Third-Party Object Compatibility** — Understands common libraries like `torch.Tensor`, `np.ndarray`, and more
- 🔄 **Ordered and Unordered Type Support** — Handles both ordered collections (e.g., `List[int, float, str, int]`) and unordered collections (e.g., `List[Union[int, float, str]]`).
---

## 📚 Examples

```python
infer_type([1, 2, 3])
# typing.List[int]

infer_type(["a", 1, 3.14])
# typing.List[typing.Union[str, int, float]]

infer_type({"name": "Alice", "age": 30})
# typing.Dict[str, Union[str, int]]

infer_type((1, "hello", 3.5), agnostic=False)
#typing.Tuple[int, str, float]

infer_type([[1, 2], [3, 4]])
# typing.List[typing.List[int]]

infer_type([torch.tensor(1), np.array(2)], agnostic=False)
#typing.List[torch.Tensor, numpy.ndarray]
```

---

## 🛠 Use Cases

- 📦 Auto-generate type hints for untyped or runtime-generated data
- 🧪 Write better tests for dynamic outputs
- 🧠 Debug and inspect complex runtime object structures

---


## 🙌 Contributing

Contributions are welcome! If you have an idea, bug, or feature request, feel free to [open an issue](https://github.com/Mikyx-1/typepeek/issues) or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 👤 Author

👨‍💻 Le Hoang Viet  
🐙 GitHub: [Mikyx-1](https://github.com/Mikyx-1)