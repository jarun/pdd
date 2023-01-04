PREFIX ?= /usr/local
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
MANDIR ?= $(DESTDIR)$(PREFIX)/share/man/man1
DOCDIR ?= $(DESTDIR)$(PREFIX)/share/doc/pdd

.PHONY: all install uninstall install-bin install-completions install-bash-completion install-zsh-completion install-fish-completion

all:

install: install-bin install-completions

install-bin:
	gzip -c pdd.1 > pdd.1.gz
	install -Dm755 pdd $(BINDIR)/pdd
	install -Dm644 pdd.1.gz $(MANDIR)
	install -Dm644 README.md $(DOCDIR)
	rm -f pdd.1.gz

install-completions: install-bash-completion install-zsh-completion install-fish-completion

install-bash-completion:
	install -Dm644 auto-completion/bash/pdd.bash $(PREFIX)/share/bash-completion/completions/pdd

install-fish-completion:
	install -Dm644 auto-completion/fish/pdd.fish -t $(PREFIX)/share/fish/vendor_completions.d

install-zsh-completion:
	cp pdd pdd.py
	auto-completion/zsh/zsh_completion.py
	install -Dm644 _pdd -t $(PREFIX)/share/zsh/site-functions

uninstall:
	rm -f $(BINDIR)/pdd
	rm -f $(MANDIR)/pdd.1.gz
	rm -rf $(DOCDIR)
	rm -rf $(PREFIX)/share/bash-completion/completions/pdd
	rm -rf $(PREFIX)/share/fish/vendor_completions.d/pdd.fish
	rm -rf $(PREFIX)/share/zsh/site-functions/_pdd

check:
	@python3 -m pytest test.py
