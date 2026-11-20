# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2024-present ROCKNIX (https://github.com/ROCKNIX)

PKG_NAME="bslap-retroarch"
PKG_VERSION="9e1c1e8ac897625ed75920019f4f62a173a4eedf"
PKG_SHA256="0d9a7c3acf988fe06f0fc7b27f72ad65adaa8b7e6681fbda48e4f59ac1883f1b"
PKG_SITE="https://github.com/libretro/RetroArch"
PKG_URL="${PKG_SITE}/archive/${PKG_VERSION}.tar.gz"
PKG_LICENSE="GPL-3.0-or-later"
PKG_DEPENDS_TARGET="toolchain SDL2 alsa-lib libass openssl freetype zlib retroarch-assets core-info ffmpeg libass joyutils nss-mdns openal-soft libogg libvorbisidec libvorbis libvpx libpng libdrm pulseaudio miniupnpc flac xz"
PKG_LONGDESC="Isolated pinned RetroArch frontend for Bslap link sessions"
PKG_BUILD_FLAGS=" +lto"

if [ "${PIPEWIRE_SUPPORT}" = "yes" ]; then
  PKG_DEPENDS_TARGET+=" pipewire"
fi

case ${ARCH} in
  arm)
    true
    ;;
  *)
    PKG_DEPENDS_TARGET+=" empty"
    ;;
esac

[ "${BATTERYPLUS_SUPPORT}" = "yes" ] && PKG_PATCH_DIRS+=" batteryplus"

PKG_CONFIGURE_OPTS_TARGET="--disable-qt \
                           --enable-alsa \
                           --enable-udev \
                           --disable-opengl1 \
                           --disable-x11 \
                           --enable-zlib \
                           --enable-freetype \
                           --disable-discord \
                           --disable-vg \
                           --disable-sdl \
                           --enable-sdl2 \
                           --enable-kms \
                           --enable-ffmpeg"

case ${ARCH} in
  arm) PKG_CONFIGURE_OPTS_TARGET+=" --enable-neon" ;;
  aarch64) PKG_CONFIGURE_OPTS_TARGET+=" --disable-neon" ;;
esac

if [ "${DISPLAYSERVER}" = "wl" ]; then
  PKG_DEPENDS_TARGET+=" wayland"
  PKG_CONFIGURE_OPTS_TARGET+=" --enable-wayland"
  case ${ARCH} in
    arm)
      true
      ;;
    *)
      PKG_DEPENDS_TARGET+=" ${WINDOWMANAGER}"
      ;;
  esac
else
  PKG_CONFIGURE_OPTS_TARGET+=" --disable-wayland"
fi

if [ "${OPENGLES_SUPPORT}" = "yes" ] && [ "${PREFER_GLES}" = "yes" ]; then
  PKG_DEPENDS_TARGET+=" ${OPENGLES}"
  # --enable-opengles3 required for glcore, --enable-opengles3_1 doesn't auto-select it
  PKG_CONFIGURE_OPTS_TARGET+=" --enable-opengles --enable-opengles3 --enable-opengles3_1"
  PKG_CONFIGURE_OPTS_TARGET+=" --disable-opengl"
else
  # Full OpenGL
  PKG_DEPENDS_TARGET+=" ${OPENGL} glu libglvnd"
  PKG_CONFIGURE_OPTS_TARGET+=" --enable-opengl"
  PKG_CONFIGURE_OPTS_TARGET+=" --disable-opengles --disable-opengles3 --disable-opengles3_1 --disable-opengles3_2"
fi

if [ "${VULKAN_SUPPORT}" = "yes" ]; then
  PKG_DEPENDS_TARGET+=" ${VULKAN}"
  PKG_CONFIGURE_OPTS_TARGET+=" --enable-vulkan --enable-vulkan_display"
else
  PKG_CONFIGURE_OPTS_TARGET+=" --disable-vulkan"
fi

pre_configure_target() {
  CFLAGS+=" -DUDEV_TOUCH_SUPPORT"
  CXXFLAGS+=" -DUDEV_TOUCH_SUPPORT"
  TARGET_CONFIGURE_OPTS=""
  cd ${PKG_BUILD}
}

make_target() {
  make HAVE_UPDATE_ASSETS=0 HAVE_LIBRETRODB=1 HAVE_BLUETOOTH=0 HAVE_NETWORKING=1 HAVE_ZARCH=1 HAVE_QT=0 HAVE_LANGEXTRA=1
  [ $? -eq 0 ] && echo "(retroarch ok)" || { echo "(retroarch failed)" ; exit 1 ; }
  make -C gfx/video_filters compiler=$CC extra_flags="$CFLAGS"
  [ $? -eq 0 ] && echo "(video filters ok)" || { echo "(video filters failed)" ; exit 1 ; }
  make -C libretro-common/audio/dsp_filters compiler=$CC extra_flags="$CFLAGS"
  [ $? -eq 0 ] && echo "(audio filters ok)" || { echo "(audio filters failed)" ; exit 1 ; }
}

makeinstall_target() {
  mkdir -p ${INSTALL}/usr/libexec/bslap
  install -m 0755 ${PKG_BUILD}/retroarch ${INSTALL}/usr/libexec/bslap/retroarch
}
