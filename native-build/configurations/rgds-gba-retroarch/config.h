#ifndef QB_CONFIG_H__
#define QB_CONFIG_H__

#define PACKAGE_NAME "retroarch"
#define HAVE_7ZIP 1
#define HAVE_ACCESSIBILITY 1
/* #undef HAVE_AL */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_ALSA 1
#endif
/* #undef HAVE_ANGLE */
/* #undef HAVE_AUDIOIO */
#define HAVE_AUDIOMIXER 1
#define HAVE_AVCODEC 1
#define HAVE_AVDEVICE 1
#define HAVE_AVFORMAT 1
#define HAVE_AVUTIL 1
#define HAVE_AV_CHANNEL_LAYOUT 1
/* #undef HAVE_BEARSSL */
#define HAVE_BLISSBOX 1
/* #undef HAVE_BLUETOOTH */
#define HAVE_BSV_MOVIE 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_BUILTINGLSLANG 1
#endif
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_BUILTINSPIRV_CROSS 1
#endif
#define HAVE_C99 1
/* #undef HAVE_CACA */
#define HAVE_CC 1
#define HAVE_CC_RESAMPLER 1
#define HAVE_CDROM 1
/* #undef HAVE_CG */
#ifndef CXX_BUILD
#define HAVE_CHD 1
#endif
#define HAVE_CHEATS 1
/* #undef HAVE_CHECK */
#define HAVE_CHEEVOS 1
#define HAVE_CHEEVOS_RVZ 1
#define HAVE_COMMAND 1
#define HAVE_CONFIGFILE 1
#define HAVE_CORE_INFO_CACHE 1
#define HAVE_CRTSWITCHRES 1
#define HAVE_CRYPTO 1
#define HAVE_CXX 1
#define HAVE_CXX11 1
#define HAVE_CXX17 1
/* #undef HAVE_D3D8 */
/* #undef HAVE_D3D9 */
/* #undef HAVE_DBUS */
/* #undef HAVE_DEBUG */
/* #undef HAVE_DINPUT */
/* #undef HAVE_DISCORD */
/* #undef HAVE_DISPMANX */
#define HAVE_DRM 1
/* #undef HAVE_DRMINGW */
/* #undef HAVE_DSOUND */
#define HAVE_DSP_FILTER 1
#define HAVE_DYLIB 1
#define HAVE_DYNAMIC 1
/* #undef HAVE_DYNAMIC_EGL */
#define HAVE_EGL 1
/* #undef HAVE_EXYNOS */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_FFMPEG 1
#endif
/* #undef HAVE_FLAC */
/* #undef HAVE_FLOATHARD */
/* #undef HAVE_FLOATSOFTFP */
#define HAVE_FONTCONFIG 1
#define HAVE_FREETYPE 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_GAMEMODE 1
#endif
/* #undef HAVE_GAME_AI */
#define HAVE_GBM 1
#define HAVE_GDI 1
#define HAVE_GETADDRINFO 1
#define HAVE_GETOPT_LONG 1
#define HAVE_GFX_WIDGETS 1
#define HAVE_GLSL 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_GLSLANG 1
#endif
#define HAVE_GLSLANG_GENERICCODEGEN 1
/* #undef HAVE_GLSLANG_HLSL */
#define HAVE_GLSLANG_MACHINEINDEPENDENT 1
/* #undef HAVE_GLSLANG_OGLCOMPILER */
#define HAVE_GLSLANG_OSDEPENDENT 1
#define HAVE_GLSLANG_SPIRV 1
#define HAVE_GLSLANG_SPIRV_TOOLS 1
#define HAVE_GLSLANG_SPIRV_TOOLS_OPT 1
#define HAVE_HID 1
#define HAVE_HIDRAW 1
/* #undef HAVE_HLSL */
/* #undef HAVE_HUB75 */
#define HAVE_IFINFO 1
#define HAVE_IMAGEVIEWER 1
/* #undef HAVE_JACK */
#define HAVE_KEYCHAIN 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_KMS 1
#endif
#define HAVE_LANGEXTRA 1
/* #undef HAVE_LIBCHECK */
#define HAVE_LIBDECOR 1
#define HAVE_LIBRETRODB 1
/* #undef HAVE_LIBSHAKE */
/* #undef HAVE_LIBSMB */
/* #undef HAVE_LIBUSB */
/* #undef HAVE_LUA */
/* #undef HAVE_MALI_FBDEV */
/* #undef HAVE_MBEDTLS */
#define HAVE_MCP 1
#define HAVE_MEMFD_CREATE 1
#define HAVE_MENU 1
/* #undef HAVE_METAL */
#define HAVE_MICROPHONE 1
/* #undef HAVE_MIST */
#define HAVE_MMAP 1
/* #undef HAVE_MOC */
#define HAVE_MODELINE 1
/* #undef HAVE_MPV */
#define HAVE_NEAREST_RESAMPLER 1
/* #undef HAVE_NEON */
#define HAVE_NETPLAYDISCOVERY 1
#define HAVE_NETPLAYDISCOVERY 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_NETWORKGAMEPAD 1
#endif
#define HAVE_NETWORKING 1
#define HAVE_NETWORK_CMD 1
/* #undef HAVE_NETWORK_VIDEO */
#define HAVE_NOUNUSED 1
#define HAVE_NOUNUSED_VARIABLE 1
#define HAVE_NO_DISCORD 1
#define HAVE_NO_NEON 1
#define HAVE_NO_OPENGL 1
#define HAVE_NO_OPENGL1 1
#define HAVE_NO_QT 1
#define HAVE_NO_SDL 1
#define HAVE_NO_VG 1
#define HAVE_NO_X11 1
#define HAVE_NVDA 1
/* #undef HAVE_ODROIDGO2 */
/* #undef HAVE_OMAP */
#define HAVE_ONLINE_UPDATER 1
/* #undef HAVE_OPENDINGUX_FBDEV */
/* #undef HAVE_OPENGL */
/* #undef HAVE_OPENGL1 */
#define HAVE_OPENGLES 1
#define HAVE_OPENGLES3 1
#define HAVE_OPENGLES3_1 1
/* #undef HAVE_OPENGLES3_2 */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_OPENGL_CORE 1
#endif
/* #undef HAVE_OPENXR */
/* #undef HAVE_OSMESA */
#define HAVE_OSS 1
/* #undef HAVE_OSS_BSD */
/* #undef HAVE_OSS_LIB */
#define HAVE_OVERLAY 1
#define HAVE_PARPORT 1
#define HAVE_PATCH 1
#define HAVE_PIPEWIRE 1
#define HAVE_PIPEWIRE_STABLE 1
/* #undef HAVE_PLAIN_DRM */
/* #undef HAVE_PRESERVE_DYLIB */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_PULSE 1
#endif
/* #undef HAVE_QT */
#define HAVE_RAAC 1
#define HAVE_RAV1 1
#define HAVE_RBMP 1
#define HAVE_RCHD 1
#define HAVE_RDDS 1
#define HAVE_RETRONFS 1
#define HAVE_RETROSMB 1
#define HAVE_RETROSSL 1
#define HAVE_REWIND 1
#define HAVE_RFLAC 1
#define HAVE_RJPEG 1
#define HAVE_RMODTRACKER 1
#define HAVE_RMP3 1
#define HAVE_RMP4 1
#define HAVE_RMPEG1 1
/* #undef HAVE_ROAR */
#define HAVE_ROPUS 1
#define HAVE_RPILED 1
#define HAVE_RPNG 1
#define HAVE_RRAR 1
/* #undef HAVE_RSOUND */
#define HAVE_RTGA 1
#define HAVE_RUNAHEAD 1
#define HAVE_RVORBIS 1
#define HAVE_RVP9 1
#define HAVE_RWAV 1
#define HAVE_RWEBM 1
#define HAVE_RWEBP 1
#define HAVE_RZSTD 1
/* #undef HAVE_SAPI */
#define HAVE_SCREENSHOTS 1
/* #undef HAVE_SDL */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_SDL2 1
#endif
/* #undef HAVE_SDL3 */
/* #undef HAVE_SDL_DINGUX */
#define HAVE_SHADERPIPELINE 1
/* #undef HAVE_SIXEL */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_SLANG 1
#endif
/* #undef HAVE_SMBCLIENT */
/* #undef HAVE_SOCKET_LEGACY */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_SPIRV_CROSS 1
#endif
/* #undef HAVE_SR2 */
#define HAVE_SSA 1
/* #undef HAVE_SSE */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_SSL 1
#endif
#define HAVE_STB_IMAGE 1
#define HAVE_STDIN_CMD 1
/* #undef HAVE_STEAM */
/* #undef HAVE_SUNXI */
#define HAVE_SWRESAMPLE 1
#define HAVE_SWSCALE 1
#define HAVE_SYSTEMD 1
#define HAVE_TEST_DRIVERS 1
#define HAVE_THREADS 1
#define HAVE_THREAD_STORAGE 1
#define HAVE_TINYALSA 1
#define HAVE_TRANSLATE 1
#define HAVE_UDEV 1
#define HAVE_UPDATE_ASSETS 1
#define HAVE_UPDATE_CORES 1
#define HAVE_UPDATE_CORE_INFO 1
/* #undef HAVE_V4L2 */
/* #undef HAVE_VC_TEST */
/* #undef HAVE_VG */
/* #undef HAVE_VIDEOCORE */
/* #undef HAVE_VIDEOPROCESSOR */
#define HAVE_VIDEO_FILTER 1
/* #undef HAVE_VIVANTE_FBDEV */
#if __cplusplus || __STDC_VERSION__ >= 199901L
#define HAVE_VULKAN 1
#endif
#define HAVE_VULKAN_DISPLAY 1
#if __cplusplus || __STDC_VERSION__ >= 199901L
#ifndef CXX_BUILD
#define HAVE_WAYLAND 1
#endif
#endif
#define HAVE_WAYLAND_CURSOR 1
#define HAVE_WAYLAND_PROTOS 1
#define HAVE_WAYLAND_SCANNER 1
/* #undef HAVE_WEBMPLAYER */
/* #undef HAVE_WIFI */
#define HAVE_WINRAWINPUT 1
/* #undef HAVE_X11 */
#define HAVE_XDELTA 1
/* #undef HAVE_XINERAMA */
/* #undef HAVE_XINPUT */
#define HAVE_XKBCOMMON 1
/* #undef HAVE_XRANDR */
/* #undef HAVE_XSHM */
/* #undef HAVE_XVIDEO */
#define HAVE_ZLIB 1
#endif
