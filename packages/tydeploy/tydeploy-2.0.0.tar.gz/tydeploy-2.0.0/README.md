# TyDeploy

TyDeploy 是以 [洛天依](https://zh.moegirl.org.cn/%E6%B4%9B%E5%A4%A9%E4%BE%9D) 命名的轻量化本地部署系统。通过 TOML 配置文件，实现本地到本地或远程的批量部署。



## 支持的部署目标

- SSH (SFTP)
- 腾讯云对象存储 (COS)
- 本地文件系统 (FS)
- 打包为压缩文件



## 用法

使用如下命令进行安装：

```shell
pip install tydeploy
```



TyDeploy 通过读取当前工作目录下的 `.tydeploy.toml` 配置文件来工作。配置文件的示例，可以在代码仓库的 `test/.tydeploy.toml.example` 中找到。

在命令行输入 `tydeploy -h` 获取帮助。



## 许可

本项目以 GPL3.0+ 许可证发布