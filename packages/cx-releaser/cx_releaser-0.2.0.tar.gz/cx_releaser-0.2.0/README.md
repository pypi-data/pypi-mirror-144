# CX Releaser

Package to interact with docker registries

Examples:

1. Create new release with recently build image

```python
from cx_releaser.src.release import Release
new_release = Release.from_remote('my_image')
new_release.next().push()
```

2. Rollback recently created release

```python
from cx_releaser.src.release import Release
all_releases = Release.get_all_from_remote('my_image')
last, prev = all_releases[0], all_releases[1]
last.rollback(prev)
```

## Command line script
