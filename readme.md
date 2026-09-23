# Awesome Mach [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<a href="https://machlang.org"><img src="media/logo.svg" align="right" width="100" alt="Mach"></a>

> Statically typed, compiled systems programming language with no hidden behavior.

Mach is small and explicit. It has no garbage collector and no hidden allocation, and a single self-hosted toolchain builds, links, tests, formats, vendors dependencies, and cross-compiles.

## Contents

- [Official Resources](#official-resources)
- [Editor Support](#editor-support)
- [Tooling](#tooling)
- [Web Development](#web-development)
- [Networking](#networking)
- [Cryptography](#cryptography)
- [Graphics](#graphics)
- [Media](#media)
- [GUI](#gui)
- [Game Development](#game-development)

## Official Resources

- [Website](https://machlang.org) - Home of the language, with install instructions.
- [Documentation](https://machlang.org/docs/) - Language reference, written to be read front to back.
- [Compiler](https://github.com/briar-systems/mach) - Self-hosted compiler, code generators, and linker with no external dependencies.
- [Standard Library](https://github.com/briar-systems/mach-std) - Allocators, collections, I/O, filesystem, formatting, and platform support.
- [Discord](https://discord.com/invite/dfWG9NhGj7) - Official community chat.

## Editor Support

- [mach-lsp](https://github.com/briar-systems/mach-lsp) - Language server built on the compiler's own frontend, with diagnostics, navigation, rename, and call hierarchy.
- [mach-vscode](https://github.com/briar-systems/mach-vscode) - Visual Studio Code extension.
- [mach-zed](https://github.com/briar-systems/mach-zed) - Zed extension with highlighting, indentation, and code outline.
- [mach-tree-sitter](https://github.com/briar-systems/mach-tree-sitter) - Tree-sitter grammar.

## Tooling

- [mach-template](https://github.com/briar-systems/mach-template) - Project starter with library layout, tiered CI, and tag-driven releases.

## Web Development

- [hedge](https://github.com/briar-systems/hedge) - Production web server.
- [laurel](https://github.com/briar-systems/laurel) - Web application framework.

## Networking

- [mach-http](https://github.com/briar-systems/mach-http) - HTTP protocol engines.
- [mach-tls](https://github.com/briar-systems/mach-tls) - TLS implementation.
- [mach-quic](https://github.com/briar-systems/mach-quic) - QUIC transport.
- [mach-acme](https://github.com/briar-systems/mach-acme) - ACME client for automated certificate issuance.
- [mach-mqtt](https://github.com/briar-systems/mach-mqtt) - MQTT 3.1.1 protocol library and broker.

## Cryptography

- [mach-crypto](https://github.com/briar-systems/mach-crypto) - Cryptographic primitives.

## Graphics

- [mach-gl](https://github.com/briar-systems/mach-gl) - OpenGL 4.6 core bindings generated from the Khronos registry.
- [mach-vk](https://github.com/briar-systems/mach-vk) - Vulkan API declarations.
- [mach-glfw](https://github.com/briar-systems/mach-glfw) - GLFW 3.4 bindings for windows, input, and contexts.
- [mach-shader](https://github.com/briar-systems/mach-shader) - Shader math that lowers to GLSL.std.450 on SPIR-V targets.

## Media

- [mach-image](https://github.com/briar-systems/mach-image) - Image decoding and encoding.
- [mach-font](https://github.com/briar-systems/mach-font) - TrueType parsing and rasterization.
- [mach-gltf](https://github.com/briar-systems/mach-gltf) - glTF 2.0 loader.
- [mach-audio](https://github.com/briar-systems/mach-audio) - Audio device output with mixing and DSP.

## GUI

- [blit](https://github.com/briar-systems/blit) - Immediate-mode GUI library.

## Game Development

- [boom](https://github.com/briar-systems/boom) - 2D-first, 3D-capable game engine.
- [mach-phys](https://github.com/briar-systems/mach-phys) - 2D and 3D physics.

## Contributing

Contributions are welcome. Read the [contribution guidelines](contributing.md) first.
