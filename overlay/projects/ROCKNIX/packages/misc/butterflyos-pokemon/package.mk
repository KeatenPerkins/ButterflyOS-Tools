# SPDX-License-Identifier: GPL-2.0-or-later
PKG_NAME="butterflyos-pokemon"
PKG_VERSION="0.1.0-rgds"
PKG_LICENSE="GPL-2.0-or-later AND MIT AND BSD-3-Clause"
PKG_URL=""
PKG_DEPENDS_TARGET="toolchain Python3 SDL2 SDL2_ttf dejavu dialog pksav bslap-backend"
PKG_TOOLCHAIN="manual"
PKG_LONGDESC="Blink, Bdex and Bslap with shared portable save and sprite tools"
make_target() {
  ${CC} ${CFLAGS} ${CPPFLAGS} -I${SYSROOT_PREFIX}/usr/include \
    -o butterflyos-save-trade ${PKG_DIR}/sources/butterflyos-save-trade.c \
    -L${SYSROOT_PREFIX}/usr/lib -Wl,-Bstatic -lpksav -Wl,-Bdynamic -lm
}
makeinstall_target() {
  mkdir -p ${INSTALL}/usr/share/licenses/butterflyos-pokemon
  install -m 0644 ${PKG_DIR}/licenses/* ${INSTALL}/usr/share/licenses/butterflyos-pokemon/
  mkdir -p ${INSTALL}/usr/bin ${INSTALL}/usr/share/butterflyos \
    ${INSTALL}/usr/config/modules/images
  install -m 0755 ${PKG_DIR}/sources/*.py ${PKG_BUILD}/butterflyos-save-trade ${INSTALL}/usr/bin/
  install -m 0644 ${PKG_DIR}/sources/*.json ${INSTALL}/usr/bin/
  install -m 0755 ${PKG_DIR}/sources/*.sh ${INSTALL}/usr/share/butterflyos/
  install -m 0644 ${PKG_DIR}/sources/*.gptk ${PKG_DIR}/sources/*.dialogrc ${INSTALL}/usr/share/butterflyos/
  cp -a ${PKG_DIR}/sources/bdex-web ${INSTALL}/usr/bin/
  install -m 0755 ${PKG_DIR}/sources/launchers/* ${INSTALL}/usr/config/modules/
  install -m 0644 ${PKG_DIR}/sources/images/*.png ${INSTALL}/usr/config/modules/images/
}
