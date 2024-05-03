all:

install:
	# Custom wallpapers
	install -d -m 755 $(DESTDIR)/usr/share/backgrounds/gnome-local-custom/
	install -m 644 wallpapers/*jpg $(DESTDIR)/usr/share/backgrounds/gnome-local-custom/
	# Manifest for wallpapers
	install -d -m 755 $(DESTDIR)/usr/share/gnome-background-properties/
	python3 scripts/properties-xml.py wallpapers | tee $(DESTDIR)/usr/share/gnome-background-properties/gnome-local-custom.xml
	# Dconf profiles
	install -d -m 755 $(DESTDIR)/usr/share/gnome-local-custom/dconf/profile
	install -m 644 dconf/profile/* $(DESTDIR)/usr/share/gnome-local-custom/dconf/profile
	# Dconf policies
	install -d -m 755 $(DESTDIR)/usr/share/gnome-local-custom/dconf/db/local.d
	install -d -m 755 $(DESTDIR)/usr/share/gnome-local-custom/dconf/db/gdm.d
	install -m 644 dconf/db/gdm.d/* $(DESTDIR)/usr/share/gnome-local-custom/dconf/db/gdm.d
	install -m 644 dconf/db/local.d/* $(DESTDIR)/usr/share/gnome-local-custom/dconf/db/local.d
	# Compile gresources
	python3 scripts/manifest.py theme/extracted | tee theme/gnome-shell-theme.gresource.xml
	glib-compile-resources theme/gnome-shell-theme.gresource.xml --sourcedir=theme/extracted --target=$(DESTDIR)/usr/share/gnome-local-custom/gnome-shell-theme.gresource

package_build:
	dpkg-buildpackage -uc -us -A
