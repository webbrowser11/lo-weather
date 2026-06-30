import automation
import api_builder

print("====================================")
print("🛠️ STARTING FULL SYSTEM TEST...")
print("====================================")

# 1. Test the API Builder
print("🧪 Testing API Builder...")
api_builder.refresh_api(push_to_git=False)
print("✅ API file generated.")

# 2. Test the HTML History Builder
print("\n🧪 Testing HTML History Builder...")
automation.build_static_html_files(push_to_git=False)
print("✅ HTML files generated.")

print("\n====================================")
print("Done! Check your 'api/' and 'site/' folders.")
print("====================================")