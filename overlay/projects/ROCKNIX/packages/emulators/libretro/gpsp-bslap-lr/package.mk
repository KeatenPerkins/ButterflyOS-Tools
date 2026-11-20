# SPDX-License-Identifier: GPL-2.0-only
PKG_NAME="gpsp-bslap-lr"
PKG_VERSION="5819380c2ffb0900219d700a382ee68c464ebb99"
PKG_LICENSE="GPL-2.0-only"
PKG_SITE="https://github.com/libretro/gpsp"
PKG_URL="${PKG_SITE}/archive/${PKG_VERSION}.tar.gz"
PKG_DEPENDS_TARGET="toolchain"
PKG_TOOLCHAIN="manual"
PKG_LONGDESC="Isolated Bslap GBA link core"
make_target() {
  make platform=unix CPU_ARCH=arm64 HAVE_DYNAREC=1 CC="${CC}" CXX="${CXX}" AR="${AR}"
}
makeinstall_target() {
  mkdir -p ${INSTALL}/usr/lib/libretro
  install -m 0755 gpsp_libretro.so ${INSTALL}/usr/lib/libretro/gpsp_bslap_libretro.so
}
