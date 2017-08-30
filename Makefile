PREFIX ?= /usr/local
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
MANDIR ?= $(DESTDIR)$(PREFIX)/share/man/man1
DOCDIR ?= $(DESTDIR)$(PREFIX)/share/doc/pdd

.PHONY: all install uninstall

all:

install:
	install -m755 -d $(BINDIR)
	install -m755 -d $(MANDIR)
	install -m755 -d $(DOCDIR)
	gzip -c pdd.1 > pdd.1.gz
	install -m755 pdd $(BINDIR)
	install -m644 pdd.1.gz $(MANDIR)
	install -m644 README.md $(DOCDIR)
	rm -f pdd.1.gz

uninstall:
	rm -f $(BINDIR)/pdd
	rm -f $(MANDIR)/pdd.1.gz
	rm -rf $(DOCDIR)

test: ;
