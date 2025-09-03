from mkdocs_macros.plugin import MacrosPlugin

def define_env(env):
	links = env.conf['extra']['links']  # ambil dari mkdocs.yml

	@env.macro
	def link(alias):
		path = links.get(alias, f"#broken-link-{alias}")
		print(f"[DEBUG] alias={alias}, raw={path}")  # console log

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
