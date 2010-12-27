# Tokyo Cabinet: a modern implementation of DBM
# http://fallabs.com/tokyocabinet/
# GPL, LGPL, BSD, Apache, etc.

include ../../Library/Rules.mk

TITLE=		Tokyo Cabinet $(VERSION)
NAME=		tokyocabinet
VERSION=	1.4.46
REVISION=	0
URL=		http://fallabs.com/tokyocabinet/
SOURCE=		$(NAME)-$(VERSION).tar.gz

README=		$(BUILDDIR)/README
LICENSE=	$(BUILDDIR)/COPYING

ifdef STATIC_ONLY
CONFIG_OPTS=	--enable-static --disable-shared
else
CONFIG_OPTS=	--disable-static --enable-shared
endif

prep: retrieve
	tar zxf $(SOURCE)
	touch prep

build: prep $(DEPENDS)
	cd $(BUILDDIR) ; env CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" \
	$(configure) $(CONFIG_OPTS) ; $(make)
	touch build

install: build
	cd $(BUILDDIR) ; make DESTDIR=$(INSTALLDIR) install
	#cd $(BUILDDIR) ; make prefix=$(INSTALLDIR)/usr/local install
	rm -f $(INSTALLDIR)/usr/local/share/info/dir
	rm -f $(INSTALLDIR)/usr/local/lib/charset.alias
	rm -f $(INSTALLDIR)/usr/local/share/locale/locale.alias
	install -d $(INSTALLDOCDIR)
	install -m 644 $(README) $(INSTALLDOCDIR)
	install -m 644 $(LICENSE) $(INSTALLDOCDIR)
	#install -m 644 $(BUILDDIR)/{ChangeLog,doc/*} $(INSTALLDOCDIR)
ifndef STATIC_ONLY
	strip -x $(INSTALLDIR)/usr/local/lib/lib*.dylib
endif
	#strip -x $(INSTALLDIR)/usr/local/lib/lib*.a
	touch install

test: install
ifndef STATIC_ONLY
	for x in $(wildcard $(INSTALLDIR)/usr/local/lib/*.dylib) ; do \
		lipo $$x -verify_arch i386 x86_64 ; done
endif
	for x in $(wildcard $(INSTALLDIR)/usr/local/lib/*.a) ; do \
		lipo $$x -verify_arch i386 x86_64 ; done
	cd $(BUILDDIR) ; make check
	touch test
