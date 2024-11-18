# Итоговое решение

Чтобы разметить датасет нужно запустить контейнер с томом:

```shell
docker build -t ekanam .
docker run -v $(pwd):/app ekanam
```
