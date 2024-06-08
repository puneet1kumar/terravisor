def analyze_plan(plan: dict) -> dict:
    resource_changes = plan.get("resource_changes", [])
    summary = {"create": [], "update": [], "delete": [], "replace": []}

    for change in resource_changes:
        actions = change.get("change", ).get("actions", [])
        resource ={ "address": change.get("address"), "type": change.get("type"), "name": change.get("name"), "actions": actions}
        
        if "create" in actions:
            summary["create"].append (resource)
        if "update" in actions:
            summary["update"]. append(resource)
        if "delete" in actions:
            summary["delete"]. append(resource)
        if "replace" in actions:
            summary[ "replace"]. append(resource)
    print(summary)
    for action, resources in summary.items():
        print("ACTION:", action.capitalize(), ":")
        for resource in resources:
            print("Type:", resource['type'],"====== Resource", resource['name'],"======= Address", resource['address'])
        print()
        print()
    return summary