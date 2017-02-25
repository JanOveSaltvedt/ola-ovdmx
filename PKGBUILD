pkgname=ola-ovdmx-git
pkgver=0.9.7.r1422.g90ee02a9b
pkgrel=1
pkgdesc="The Open Lighting Architecture (OLA) provides a plugin framework for distributing DMX512 control signals on Mac and Linux. Includes the OVdmx plugin"
arch=('i686' 'x86_64')
url="https://www.openlighting.org/ola/"
license=('LGPL2.1' 'GPL2')
provides=('ola')
makedepends=('git')
depends=('libmicrohttpd' 'cppunit' 'protobuf' 'python2-protobuf' 'python2')
optdepends=('liblo' 'avahi' 'libusb' 'libusb-compat' 'libftdi-compat' 'openslp' 'flex' 'bison')
conflicts=('ola')
source=("git+https://github.com/JanOveSaltvedt/ola-ovdmx.git")
sha256sums=('SKIP')

_gitname="ola-ovdmx"

pkgver() {
	cd "${srcdir}/${_gitname}"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "${srcdir}/${_gitname}"
  
  autoreconf -i
	# since protobuf isnt ported to python 3 we have to choose python 2 
	PYTHON=python2 ./configure --prefix=/usr --enable-python-libs --disable-unittests --disable-fatal-warnings
	make
}

package() {
	make -C "${srcdir}/${_gitname}" DESTDIR="${pkgdir}" install
}
