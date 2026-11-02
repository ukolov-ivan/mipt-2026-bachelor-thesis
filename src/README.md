This projects uses forked version of [`tikzplotlib`](https://github.com/nschloe/tikzplotlib) with some various tiny fixes, since the original repository and corresponding package are abandoned.

To install dependencies with a remote version of the `tikzplotlib` fork usual `pip install -r requirements.txt` command can be used.

To install dependencies with local `tikzplotlib` package fork via

```sh
pip install -r requirements.local.txt
```

repo must be cloned with its submodules:

```sh
git clone --recurse-submodules <url>
```

Or, if already cloned, fetching of submodules can be done with:

```sh
git submodule update --init --recursive
```
