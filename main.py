from mkdocs_macros.plugin import MacrosPlugin
from mkdocs.config.defaults import get_schema

def define_env(env):
	assets = env.conf['extra']['assets']  # ambil dari mkdocs.yml
	links = env.conf['extra']['links']  # ambil dari mkdocs.yml

	# helper buat ambil nested key pakai dot notation
	def get_nested(d, keys, default=None):
		for key in keys.split('.'):
			if isinstance(d, dict) and key in d:
				d = d[key]
			else:
				return default
		return d

	@env.macro
	def asset(alias):
		path = get_nested(assets, alias, f"#broken-link-{alias}")

		# kalau link sudah absolute atau anchor biarin
		if path.startswith(("http://", "https://", "#", "/")):
			return path
		return "/" + path.lstrip("/")

	# @env.macro
	# def asset(alias):
	# 	path = get_nested(assets, alias, f"#broken-link-{alias}")
	# 	if path.startswith(("http://", "https://", "#")):
	# 		return path
	# 	return f"{env.conf['use_directory_urls'] and '' or '.'}/{path.lstrip('/')}"

	# @env.macro
	# def asset(alias):
	# 	path = get_nested(assets, alias, f"#broken-link-{alias}")
	# 	if path.startswith(("http://", "https://", "#", "/")):
	# 		return path
	# 	return path  # biarin relative aja

	# def asset(alias):
	# 	path = get_nested(assets, alias, f"#broken-link-{alias}")
	# 	# print(f"[DEBUG] alias={alias}, raw={path}")

	# 	# kalau link sudah absolute (http, https, #), biarin
	# 	if path.startswith(("http://", "https://", "#")):
	# 		return path

	# 	# jangan tambahin "/" di depan → biar relative
	# 	return path

	@env.macro
	def image_grid(images, width="200", height="150"):
		"""
		Generate grid horizontal dengan gambar + caption.
		Semua gambar dipaksa punya tinggi sama (object-fit cover).

		images = list of (alias, caption)
		width  = lebar gambar (default 200px)
		height = tinggi gambar (default 150px)
		"""
		items = []
		for alias, caption in images:
			src = asset(alias)
			item_html = f"""
<figure style="text-align: center; margin: 10px;">
	<img src="{src}" alt="{caption}"
		style="border-radius: 8px;
			box-shadow: 0px 0px 2px 0.5px rgba(255, 143, 0, 0.6);
			width: {width}px;
			height: {height}px;">
	<figcaption>{caption}</figcaption>
</figure>
"""
			items.append(item_html)

		# bungkus pakai flexbox biar dalam 1 row
		html = f"""
<div style="display: flex; justify-content: center; flex-wrap: wrap;">
	{''.join(items)}
</div>
"""
		return html


	@env.macro
	def image_with_caption(alias, caption, width="400"):
		"""
		Generate <figure> dengan gambar + caption center.
		alias   = key di mkdocs.yml extra.assets
		caption = teks di bawah gambar
		width   = optional (default 400px)
		"""
		src = asset(alias)
		html = f"""
<figure style="text-align: center;">
  <img src="{src}" alt="{caption}" width="{width}" style="border-radius: 8px; box-shadow: 0px 0px 2px 0.5px rgba(255, 143, 0, 0.6);">
  <figcaption>{caption}</figcaption>
</figure>
"""
		return html

	@env.macro
	def link(alias):
		path = links.get(alias, f"#broken-link-{alias}")

		# kalau link sudah http/https/# biarin aja
		if path.startswith(("http://", "https://", "#")):
			return path

		# tambahkan "/" di depan biar absolute
		result = path.replace(".md", "/")  # absolute + friendly URL
		return "/" + result.lstrip("/")

	@env.macro
	# Make text small
	def small(text):
		# Ganti semua backtick (`) dengan HTML entity supaya aman
		# safe_text = text.replace("`", "&#96;")
		# safe_text = text
		# return f"<small>{safe_text}</small>"

		# Render isi text dengan macro lagi (supaya {{ code() }} diproses)
		rendered = MacrosPlugin.render(env, text)
		return f"<small>{rendered}</small>"

	@env.macro
	def code(text):
		return f"<code>{text}</code>"

	@env.macro
	def h1(text):
		return f"<span style='font-size: 32px;'>{text}</span>"
	@env.macro
	def h2(text):
		return f"<span style='font-size: 24px;'>{text}</span>"
	@env.macro
	def h3(text):
		return f"<span style='font-size: 18.72px;'>{text}</span>"
	@env.macro
	def h4(text):
		return f"<span style='font-size: 16px;'>{text}</span>"
	@env.macro
	def h5(text):
		return f"<span style='font-size: 13.28px;'>{text}</span>"
	@env.macro
	def h6(text):
		return f"<span style='font-size: 10.72px;'>{text}</span>"


# 	@env.macro
# 	def setup_nav(component, current_section):
# 		"""Generate setup navigation for a component"""
# 		sections = ['installation', 'configuration', 'start']
# 		nav_items = []

# 		for section in sections:
# 			if section != current_section:
# 				emoji = {'installation': '📦', 'configuration': '⚙️', 'start': '🚀'}[section]
# 				nav_items.append(f"[{emoji} {section.title()}](../{section}/{component}.md)")

# 		return " | ".join(nav_items)

# 	@env.macro
# 	def component_matrix():
# 		"""Generate component comparison matrix"""
# 		return """
# | Action | Grafana | Prometheus |
# |--------|---------|------------|
# | Install | [📦 Install](../installation/grafana.md) | [📦 Install](../installation/prometheus.md) |
# | Configure | [⚙️ Config](../configuration/grafana.md) | [⚙️ Config](../configuration/prometheus.md) |
# | Start | [🚀 Start](../start/grafana.md) | [🚀 Start](../start/prometheus.md) |
# """
