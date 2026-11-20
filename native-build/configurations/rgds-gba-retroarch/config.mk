CC = /build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/bin/aarch64-rocknix-linux-gnu-gcc
CFLAGS = -march=armv8.2-a+crc+crypto+fp+simd+rcpc -mabi=lp64 -Wno-psabi -mtune=cortex-a55 -mno-outline-atomics -Wall -pipe  -flto -fno-fat-lto-objects -O2 -fomit-frame-pointer -DNDEBUG -DUDEV_TOUCH_SUPPORT
CXX = /build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/bin/aarch64-rocknix-linux-gnu-g++
CXXFLAGS = -march=armv8.2-a+crc+crypto+fp+simd+rcpc -mabi=lp64 -Wno-psabi -mtune=cortex-a55 -mno-outline-atomics -Wall -pipe  -flto -fno-fat-lto-objects -O2 -fomit-frame-pointer -DNDEBUG -DUDEV_TOUCH_SUPPORT
WINDRES = 
MOC = 
ASFLAGS = 
LDFLAGS =  -Wl,--as-needed -fuse-ld=bfd
INCLUDE_DIRS = 
LIBRARY_DIRS = -L/usr/lib64
PACKAGE_NAME = retroarch
BUILD = 
PREFIX = /usr/local
HAVE_7ZIP = 1
HAVE_ACCESSIBILITY = 1
HAVE_AL = 0
ifneq ($(C89_BUILD),1)
HAVE_ALSA = 1
endif
ALSA_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
ALSA_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lasound
HAVE_ANGLE = 0
HAVE_AUDIOIO = 0
HAVE_AUDIOMIXER = 1
HAVE_AVCODEC = 1
AVCODEC_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
AVCODEC_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lavcodec
HAVE_AVDEVICE = 1
AVDEVICE_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
AVDEVICE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lavdevice
HAVE_AVFORMAT = 1
AVFORMAT_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
AVFORMAT_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lavformat
HAVE_AVUTIL = 1
AVUTIL_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
AVUTIL_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lavutil
HAVE_AV_CHANNEL_LAYOUT = 1
HAVE_BEARSSL = 0
HAVE_BLISSBOX = 1
HAVE_BLUETOOTH = 0
HAVE_BSV_MOVIE = 1
ifneq ($(C89_BUILD),1)
HAVE_BUILTINGLSLANG = 1
endif
ifneq ($(C89_BUILD),1)
HAVE_BUILTINSPIRV_CROSS = 1
endif
HAVE_C99 = 1
C99_CFLAGS = -std=gnu99
HAVE_CACA = 0
HAVE_CC = 1
HAVE_CC_RESAMPLER = 1
HAVE_CDROM = 1
HAVE_CG = 0
ifneq ($(CXX_BUILD),1)
HAVE_CHD = 1
endif
HAVE_CHEATS = 1
HAVE_CHECK = 0
HAVE_CHEEVOS = 1
HAVE_CHEEVOS_RVZ = 1
HAVE_COMMAND = 1
HAVE_CONFIGFILE = 1
HAVE_CORE_INFO_CACHE = 1
HAVE_CRTSWITCHRES = 1
HAVE_CRYPTO = 1
HAVE_CXX = 1
HAVE_CXX11 = 1
CXX11_CFLAGS = -std=c++11
HAVE_CXX17 = 1
CXX17_CFLAGS = -std=c++17
HAVE_D3D8 = 0
HAVE_D3D9 = 0
HAVE_DBUS = 0
HAVE_DEBUG = 0
HAVE_DINPUT = 0
HAVE_DISCORD = 0
HAVE_DISPMANX = 0
HAVE_DRM = 1
DRM_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/libdrm
DRM_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -ldrm
HAVE_DRMINGW = 0
HAVE_DSOUND = 0
HAVE_DSP_FILTER = 1
HAVE_DYLIB = 1
DYLIB_LIBS = -ldl
HAVE_DYNAMIC = 1
DYNAMIC_LIBS = -ldl
HAVE_DYNAMIC_EGL = 0
HAVE_EGL = 1
EGL_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
EGL_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lEGL
HAVE_EXYNOS = 0
ifneq ($(C89_BUILD),1)
HAVE_FFMPEG = 1
endif
HAVE_FLAC = 0
HAVE_FLOATHARD = 0
HAVE_FLOATSOFTFP = 0
HAVE_FONTCONFIG = 1
FONTCONFIG_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/freetype2 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
FONTCONFIG_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lfontconfig -lfreetype
HAVE_FREETYPE = 1
FREETYPE_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/freetype2 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
FREETYPE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lfreetype
ifneq ($(C89_BUILD),1)
HAVE_GAMEMODE = 1
endif
HAVE_GAME_AI = 0
HAVE_GBM = 1
GBM_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
GBM_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lgbm
HAVE_GDI = 1
HAVE_GETADDRINFO = 1
GETADDRINFO_LIBS = -lc
HAVE_GETOPT_LONG = 1
GETOPT_LONG_LIBS = -lc
HAVE_GFX_WIDGETS = 1
HAVE_GLSL = 1
ifneq ($(C89_BUILD),1)
HAVE_GLSLANG = 1
endif
GLSLANG_LIBS = -lglslang
HAVE_GLSLANG_GENERICCODEGEN = 1
GLSLANG_GENERICCODEGEN_LIBS = -lGenericCodeGen
HAVE_GLSLANG_HLSL = 0
HAVE_GLSLANG_MACHINEINDEPENDENT = 1
GLSLANG_MACHINEINDEPENDENT_LIBS = -lMachineIndependent
HAVE_GLSLANG_OGLCOMPILER = 0
HAVE_GLSLANG_OSDEPENDENT = 1
GLSLANG_OSDEPENDENT_LIBS = -lOSDependent
HAVE_GLSLANG_SPIRV = 1
GLSLANG_SPIRV_LIBS = -lSPIRV
HAVE_GLSLANG_SPIRV_TOOLS = 1
GLSLANG_SPIRV_TOOLS_LIBS = -lSPIRV-Tools
HAVE_GLSLANG_SPIRV_TOOLS_OPT = 1
GLSLANG_SPIRV_TOOLS_OPT_LIBS = -lSPIRV-Tools-opt
HAVE_HID = 1
HAVE_HIDRAW = 1
HAVE_HLSL = 0
HAVE_HUB75 = 0
HAVE_IFINFO = 1
HAVE_IMAGEVIEWER = 1
HAVE_JACK = 0
HAVE_KEYCHAIN = 1
ifneq ($(C89_BUILD),1)
HAVE_KMS = 1
endif
HAVE_LANGEXTRA = 1
HAVE_LIBCHECK = 0
HAVE_LIBDECOR = 1
LIBDECOR_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/libdecor-0 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
LIBDECOR_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -ldecor-0
HAVE_LIBRETRODB = 1
HAVE_LIBSHAKE = 0
HAVE_LIBSMB = 0
HAVE_LIBUSB = 0
HAVE_LUA = 0
HAVE_MALI_FBDEV = 0
HAVE_MBEDTLS = 0
HAVE_MCP = 1
HAVE_MEMFD_CREATE = 1
MEMFD_CREATE_LIBS = -lc
HAVE_MENU = 1
HAVE_METAL = 0
HAVE_MICROPHONE = 1
HAVE_MIST = 0
HAVE_MMAP = 1
MMAP_LIBS = -lc
HAVE_MOC = 0
HAVE_MODELINE = 1
HAVE_MPV = 0
HAVE_NEAREST_RESAMPLER = 1
HAVE_NEON = 0
HAVE_NETPLAYDISCOVERY = 1
HAVE_NETPLAYDISCOVERY = 1
ifneq ($(C89_BUILD),1)
HAVE_NETWORKGAMEPAD = 1
endif
HAVE_NETWORKING = 1
NETWORKING_LIBS = -lc
HAVE_NETWORK_CMD = 1
HAVE_NETWORK_VIDEO = 0
HAVE_NOUNUSED = 1
NOUNUSED_CFLAGS = -Wno-unused-result
HAVE_NOUNUSED_VARIABLE = 1
NOUNUSED_VARIABLE_CFLAGS = -Wno-unused-variable
HAVE_NO_DISCORD = 1
HAVE_NO_NEON = 1
HAVE_NO_OPENGL = 1
HAVE_NO_OPENGL1 = 1
HAVE_NO_QT = 1
HAVE_NO_SDL = 1
HAVE_NO_VG = 1
HAVE_NO_X11 = 1
HAVE_NVDA = 1
HAVE_ODROIDGO2 = 0
HAVE_OMAP = 0
HAVE_ONLINE_UPDATER = 1
HAVE_OPENDINGUX_FBDEV = 0
HAVE_OPENGL = 0
HAVE_OPENGL1 = 0
HAVE_OPENGLES = 1
OPENGLES_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
OPENGLES_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lGLESv2
HAVE_OPENGLES3 = 1
HAVE_OPENGLES3_1 = 1
HAVE_OPENGLES3_2 = 0
ifneq ($(C89_BUILD),1)
HAVE_OPENGL_CORE = 1
endif
HAVE_OPENXR = 0
HAVE_OSMESA = 0
HAVE_OSS = 1
HAVE_OSS_BSD = 0
HAVE_OSS_LIB = 0
HAVE_OVERLAY = 1
HAVE_PARPORT = 1
HAVE_PATCH = 1
HAVE_PIPEWIRE = 1
PIPEWIRE_CFLAGS = -D_REENTRANT -fno-strict-aliasing -fno-strict-overflow -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/pipewire-0.3 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/spa-0.2
PIPEWIRE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lpipewire-0.3
HAVE_PIPEWIRE_STABLE = 1
PIPEWIRE_STABLE_CFLAGS = -D_REENTRANT -fno-strict-aliasing -fno-strict-overflow -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/pipewire-0.3 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/spa-0.2
PIPEWIRE_STABLE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lpipewire-0.3
HAVE_PLAIN_DRM = 0
HAVE_PRESERVE_DYLIB = 0
ifneq ($(C89_BUILD),1)
HAVE_PULSE = 1
endif
PULSE_CFLAGS = -D_REENTRANT -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
PULSE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lpulse -pthread
HAVE_QT = 0
HAVE_RAAC = 1
HAVE_RAV1 = 1
HAVE_RBMP = 1
HAVE_RCHD = 1
HAVE_RDDS = 1
HAVE_RETRONFS = 1
HAVE_RETROSMB = 1
HAVE_RETROSSL = 1
HAVE_REWIND = 1
HAVE_RFLAC = 1
HAVE_RJPEG = 1
HAVE_RMODTRACKER = 1
HAVE_RMP3 = 1
HAVE_RMP4 = 1
HAVE_RMPEG1 = 1
HAVE_ROAR = 0
HAVE_ROPUS = 1
HAVE_RPILED = 1
HAVE_RPNG = 1
HAVE_RRAR = 1
HAVE_RSOUND = 0
HAVE_RTGA = 1
HAVE_RUNAHEAD = 1
HAVE_RVORBIS = 1
HAVE_RVP9 = 1
HAVE_RWAV = 1
HAVE_RWEBM = 1
HAVE_RWEBP = 1
HAVE_RZSTD = 1
HAVE_SAPI = 0
HAVE_SCREENSHOTS = 1
HAVE_SDL = 0
ifneq ($(C89_BUILD),1)
HAVE_SDL2 = 1
endif
SDL2_CFLAGS = -D_REENTRANT -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/SDL2 -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
SDL2_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lSDL2
HAVE_SDL3 = 0
SDL3_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include/libdrm -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
SDL3_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lSDL3
HAVE_SDL_DINGUX = 0
HAVE_SHADERPIPELINE = 1
HAVE_SIXEL = 0
ifneq ($(C89_BUILD),1)
HAVE_SLANG = 1
endif
HAVE_SMBCLIENT = 0
HAVE_SOCKET_LEGACY = 0
ifneq ($(C89_BUILD),1)
HAVE_SPIRV_CROSS = 1
endif
HAVE_SR2 = 0
HAVE_SSA = 1
SSA_LIBS = -lfribidi -lass
HAVE_SSE = 0
ifneq ($(C89_BUILD),1)
HAVE_SSL = 1
endif
HAVE_STB_IMAGE = 1
HAVE_STDIN_CMD = 1
STDIN_CMD_LIBS = -lc
HAVE_STEAM = 0
HAVE_SUNXI = 0
HAVE_SWRESAMPLE = 1
SWRESAMPLE_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
SWRESAMPLE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lswresample
HAVE_SWSCALE = 1
SWSCALE_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
SWSCALE_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lswscale
HAVE_SYSTEMD = 1
SYSTEMD_LIBS = -lsystemd
HAVE_TEST_DRIVERS = 1
HAVE_THREADS = 1
THREADS_LIBS = -lpthread
HAVE_THREAD_STORAGE = 1
THREAD_STORAGE_LIBS = -lpthread
HAVE_TINYALSA = 1
HAVE_TRANSLATE = 1
HAVE_UDEV = 1
UDEV_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
UDEV_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -ludev
HAVE_UPDATE_ASSETS = 1
HAVE_UPDATE_CORES = 1
HAVE_UPDATE_CORE_INFO = 1
HAVE_V4L2 = 0
HAVE_VC_TEST = 0
HAVE_VG = 0
HAVE_VIDEOCORE = 0
HAVE_VIDEOPROCESSOR = 0
HAVE_VIDEO_FILTER = 1
HAVE_VIVANTE_FBDEV = 0
ifneq ($(C89_BUILD),1)
HAVE_VULKAN = 1
endif
VULKAN_LIBS = -lvulkan
HAVE_VULKAN_DISPLAY = 1
ifneq ($(C89_BUILD),1)
ifneq ($(CXX_BUILD),1)
HAVE_WAYLAND = 1
endif
endif
WAYLAND_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
WAYLAND_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lwayland-egl -lwayland-client -lm
HAVE_WAYLAND_CURSOR = 1
WAYLAND_CURSOR_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
WAYLAND_CURSOR_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lwayland-cursor
HAVE_WAYLAND_PROTOS = 1
WAYLAND_PROTOS_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
HAVE_WAYLAND_SCANNER = 1
WAYLAND_SCANNER_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/include
HAVE_WEBMPLAYER = 0
HAVE_WIFI = 0
HAVE_WINRAWINPUT = 1
HAVE_X11 = 0
HAVE_XDELTA = 1
HAVE_XINERAMA = 0
HAVE_XINPUT = 0
HAVE_XKBCOMMON = 1
XKBCOMMON_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
XKBCOMMON_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lxkbcommon
HAVE_XRANDR = 0
HAVE_XSHM = 0
HAVE_XVIDEO = 0
HAVE_ZLIB = 1
ZLIB_CFLAGS = -I/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/include
ZLIB_LIBS = -L/build/rocknix/build.ROCKNIX-RK3566.aarch64/toolchain/aarch64-rocknix-linux-gnu/sysroot/usr/lib -lz
DATA_DIR = /usr/local/share
DYLIB_LIB = -ldl
ASSETS_DIR = /usr/local/share/retroarch
FILTERS_DIR = /usr/local/share/retroarch
CORE_INFO_DIR = /usr/local/share/retroarch
BIN_DIR = /usr/local/bin
DOC_DIR = /usr/local/share/doc/retroarch
MAN_DIR = /usr/local/share/man
OS = Linux
QT_VERSION = qt5
GLOBAL_CONFIG_DIR = /etc
