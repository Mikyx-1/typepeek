## [0.2.0] - 2025-04-13

### Added
- **Ordered and Unordered Type Support** — Added handling for ordered and unordered collections like `List[int, float, float]` and `List[Union[int, float]]`.
- **Precise Type Inference** improvements for better heterogeneous and nested type handling.

### Changed
- Updated colored logging and custom formatter to include more flexibility.

### Fixed
- Addressed issues with set type inference in strict mode.

---

## [0.1.0] - 2025-04-12

### Added
- **Initial release** of the typepeek package.
- **Type inference** for basic collections like `List`, `Tuple`, and `Dict`.
- **Support for third-party objects** like `torch.Tensor` and `np.ndarray`.

