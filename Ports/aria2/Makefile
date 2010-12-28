# The Next Generation Download Utility
# http://aria2.sourceforge.net/
# GPL

include ../../Library/Rules.mk

TITLE=		aria2 $(VERSION)
NAME=		aria2
VERSION=	1.10.8
REVISION=	0
URL=		http://downloads.sourceforge.net/$(NAME)
SOURCE=		$(NAME)-$(VERSION).tar.bz2

README=		$(BUILDDIR)/README.asciidoc
LICENSE=	$(BUILDDIR)/COPYING

#ifdef WITHOUT_NLS
#CONFIG_OPTS=	--disable-nls
#else
#DEPENDS+=	/usr/local/lib/libintl.la
#CONFIG_OPTS=	--enable-nls
#endif

#ifdef WITH_STATIC_NLS
#LDFLAGS+=	-framework CoreFoundation -liconv
#endif

# Sometimes required to access FTP sites
#FETCH+=	--disable-epsv

prep: retrieve
	tar zxf $(SOURCE)
	touch prep

build: prep $(DEPENDS)
	cd $(BUILDDIR) ; $(configure) --disable-dependency-tracking ; $(make)
	#cd $(BUILDDIR) ; $(make) CFLAGS="$(CFLAGS)" LDFLAGS="($LDFLAGS)"
	touch build

#
# Install in a self-contained directory root
#
install: build
	cd $(BUILDDIR) ; make DESTDIR=$(INSTALLDIR) install
	#cd $(BUILDDIR) ; make prefix=$(INSTALLDIR)/usr/local install
	rm -f $(INSTALLDIR)/usr/local/share/info/dir
	rm -f $(INSTALLDIR)/usr/local/lib/charset.alias
	rm -f $(INSTALLDIR)/usr/local/share/locale/locale.alias
	install -d $(INSTALLDOCDIR)
	install -m 644 $(README) $(INSTALLDOCDIR)
	install -m 644 $(LICENSE) $(INSTALLDOCDIR)
	install -m 644 $(BUILDDIR)/{AUTHORS,ChangeLog,NEWS} $(INSTALLDOCDIR)
	strip $(INSTALLDIR)/usr/local/bin/*
	touch install

test: install
	for x in $(wildcard $(INSTALLDIR)/usr/local/bin/*) ; do \
		lipo $$x -verify_arch i386 x86_64 ; done
	cd $(BUILDDIR) ; make check
	touch test
