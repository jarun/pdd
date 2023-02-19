PREFIX ?= /usr/local
BINDIR ?= $(DESTDIR)$(PREFIX)/bin
SHAREDIR ?= $(DESTDIR)$(PREFIX)/share
MANDIR ?= $(SHAREDIR)/man/man1
DOCDIR ?= $(SHAREDIR)/doc/pdd

.PHONY: all install uninstall install-bin install-completions install-bash-completion install-zsh-completion install-fish-completion

all:

install: install-bin install-completions

install-bin:
	gzip -c pdd.1 > pdd.1.gz
	install -Dm755 pdd $(BINDIR)/pdd
	install -Dm644 pdd.1.gz $(MANDIR)/pdd.1.gz
	install -Dm644 README.md $(DOCDIR)/README.md
	rm -f pdd.1.gz

install-completions: install-bash-completion install-zsh-completion install-fish-completion

install-bash-completion:
	install -Dm644 auto-completion/bash/pdd.bash $(SHAREDIR)/bash-completion/completions/pdd

install-fish-completion:
	install -Dm644 auto-completion/fish/pdd.fish -t $(SHAREDIR)/fish/vendor_completions.d

install-zsh-completion:
	cp pdd pdd.py
	auto-completion/zsh/zsh_completion.py
	install -Dm644 _pdd -t $(SHAREDIR)/zsh/site-functions

uninstall:
	rm -f $(BINDIR)/pdd
	rm -f $(MANDIR)/pdd.1.gz
	rm -rf $(DOCDIR)
	rm -rf $(SHAREDIR)/bash-completion/completions/pdd
	rm -rf $(SHAREDIR)/fish/vendor_completions.d/pdd.fish
	rm -rf $(SHAREDIR)/zsh/site-functions/_pdd

check:
	@python3 -m pytest test.py
