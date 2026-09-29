# Awesome Mach [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<a href="https://machlang.org"><img src="media/logo.svg" align="right" width="100" alt="Mach"></a>

> Statically typed, compiled systems programming language with no hidden behavior.

Mach is small and explicit. It has no garbage collector and no hidden allocation, and a single self-hosted toolchain builds, links, tests, formats, vendors dependencies, and cross-compiles.

## Contents

- [Editor Support](#editor-support)
- [Web Development](#web-development)
- [Networking](#networking)
- [Cryptography](#cryptography)
- [Graphics](#graphics)
- [Media](#media)
- [GUI](#gui)
- [Game Development](#game-development)
- [Applications](#applications)
- [Resources](#resources)
  - [Learning](#learning)
  - [Community](#community)

## Editor Support

- [mach-lsp](https://github.com/briar-systems/mach-lsp) - Language server built on the compiler's own frontend, with diagnostics, navigation, rename, and call hierarchy.
- [mach-vscode](https://github.com/briar-systems/mach-vscode) - Visual Studio Code extension with syntax highlighting kept in step with the compiler.
- [mach-zed](https://github.com/briar-systems/mach-zed) - Zed extension with highlighting, indentation, code outline, and a language server it downloads to match your compiler.
- [mach-tree-sitter](https://github.com/briar-systems/mach-tree-sitter) - Tree-sitter grammar for highlighting, folding, and indentation in Neovim, Helix, Emacs, and other Tree-sitter editors.

## Web Development

- [hedge](https://github.com/briar-systems/hedge) - Web server for static files, applications, and reverse proxying over HTTP/1.1, HTTP/2, and HTTP/3, with native TLS 1.3 and ACME certificates. It serves machlang.org.
- [laurel](https://github.com/briar-systems/laurel) - Web application framework with typed handlers, middleware, sessions, CSRF protection, forms, streamed uploads, and server-sent events.

## Networking

- [mach-http](https://github.com/briar-systems/mach-http) - HTTP/1.1, HTTP/2, HTTP/3, and WebSocket engines, with a client that pools connections, follows redirects, and retries.
- [mach-tls](https://github.com/briar-systems/mach-tls) - TLS 1.2 and 1.3 clients and servers with X.509 path verification and session resumption.

## Cryptography

- [mach-crypto](https://github.com/briar-systems/mach-crypto) - SHA-2, HMAC, HKDF, AES-GCM, and ChaCha20-Poly1305 with secret-holding storage, published with its assurance evidence.

## Graphics

- [mach-glfw](https://github.com/briar-systems/mach-glfw) - GLFW 3.4 bindings for windows, input, OpenGL contexts, and Vulkan surfaces.
- [mach-gl](https://github.com/briar-systems/mach-gl) - OpenGL 4.6 core bindings generated from the Khronos registry, with an idiomatic layer over the raw calls.
- [mach-vk](https://github.com/briar-systems/mach-vk) - Vulkan declarations generated from the Khronos registry, with commands loaded at runtime and nothing linked.

## Media

- [mach-image](https://github.com/briar-systems/mach-image) - PNG, QOI, and TGA decoding and encoding with no C libraries.
- [mach-font](https://github.com/briar-systems/mach-font) - TrueType parsing and glyph rasterization into coverage bitmaps, with no FreeType.
- [mach-gltf](https://github.com/briar-systems/mach-gltf) - glTF 2.0 and GLB loader with materials, skins, animations, and morph targets.
- [mach-audio](https://github.com/briar-systems/mach-audio) - Audio output with mixing, resampling, DSP, and WAV decoding written in Mach over a minimal device layer.

## GUI

- [blit](https://github.com/briar-systems/blit) - Immediate-mode GUI that produces a draw list and leaves windowing and rendering to you.

## Game Development

- [boom](https://github.com/briar-systems/boom) - 2D-first, 3D-capable game engine with a Vulkan renderer, shaders written in Mach, and skeletal animation.

## Applications

- [machete](https://github.com/NickDrohan/machete) - UCI chess engine with a neural-network evaluation, multithreaded search, and hand-encoded AVX2 kernels, named for what it does to a variation tree.

## Resources

### Learning

- [Website](https://machlang.org) - Install instructions, the language at a glance, and the full ecosystem catalog.
- [Documentation](https://machlang.org/docs/) - Language reference written to be read front to back.

### Community

- [Discord](https://discord.com/invite/dfWG9NhGj7) - Official community chat.

## Contributing

Contributions are welcome. Read the [contribution guidelines](contributing.md) first.
