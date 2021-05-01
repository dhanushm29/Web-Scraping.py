def tips_includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
print(tips_includes_all([1, 2, 3, 4], [1, 4]))
print(tips_includes_all([1, 2, 3, 4], [1, 5]))
