# Cocos app packager

使用上传的 Cocos Creator 2.4.13 原生工程（`jsb-default`）构建 Android APK 或 iOS 未签名 IPA。源码 ZIP 不放入 Git 历史，而存放在仓库 Release `source-v1` 的附件中，以避免超大 Git 仓库。

## 构建

在 GitHub 仓库 **Actions → Build mobile packages → Run workflow** 手动启动：

- `platform`: `android`、`ios` 或 `both`
- `package_name`: 可留空以沿用项目默认 `com.bqkj.byyl`；也可填写新的反向域名标识。

成功后在 workflow run 的 **Artifacts** 下载产物。Android 输出 APK。iOS 输出未签名 IPA：没有开发者证书，因此该 IPA 仅是未签名打包结果，不能直接安装到普通 iPhone、提交 App Store 或用于 TestFlight；后续需由有证书的环境签名。

## 项目与构建约束

- Cocos Creator 2.4.13；Android 模块位于 `frameworks/runtime-src/proj.android-studio`。
- Android 采用 GitHub `ubuntu-22.04` runner、JDK 17、Android SDK 33 / Build Tools 34.0.0 / NDK 23.1.7779620，生成 debug 签名 APK。
- iOS 使用 macOS runner 和 Xcode；在不启用代码签名的情况下构建 `.app`，再封装成 `.ipa`。
- 每次 workflow 构建从私有 Release 附件拉取源码 ZIP。不要将密钥或签名证书放入仓库。

## 源码附件

Release tag: `source-v1`，附件：`jsb-default.zip`。
