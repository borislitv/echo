build docker images with

```docker build -t registry.ape.yandex.net/echo```

push to registry

```docker push registry.ape.yandex.net/echo```

upload manifest to cocaine

```cocaine-tool app upload -n echo --manifest-only --manifest ./manifest```

start app

```cocaine-tool app start -n echo --profile docker-nocold --timeout 100```
