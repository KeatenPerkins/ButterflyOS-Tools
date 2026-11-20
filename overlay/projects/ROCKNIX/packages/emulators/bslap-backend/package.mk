# SPDX-License-Identifier: GPL-2.0-or-later
PKG_NAME="bslap-backend"
PKG_VERSION="0.1.0-rgds"
PKG_LICENSE="GPL-3.0-or-later AND GPL-2.0-only"
PKG_URL=""
PKG_DEPENDS_TARGET="toolchain Python3:host bslap-retroarch gpsp-bslap-lr gambatte-bslap-lr sameboy-lr core-info"
PKG_TOOLCHAIN="manual"
PKG_LONGDESC="RG DS isolated Bslap link runtime and integrity manifest"
PKG_NEED_UNPACK="$(get_pkg_directory bslap-retroarch) $(get_pkg_directory gpsp-bslap-lr) $(get_pkg_directory gambatte-bslap-lr) $(get_pkg_directory sameboy-lr)"
makeinstall_target() {
  python3 ${PKG_DIR}/sources/stage.py ${BUILD}/install_pkg ${INSTALL}
}
