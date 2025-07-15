from tools.extract_engaged_users import extract_engaged_users
from tools.generate_outreach_message import generate_outreach_messages
from tools.generate_competitor_companies import discover_competitors

if __name__ == "__main__":

    print("\n🔍 Discovering competitor companies...")
    # Less strict, more general company description for broader competitor discovery
    company_description = (
        "Workerbase provides digital tools and workflow automation for frontline workers in manufacturing. "
        "Our platform helps companies improve efficiency, reduce downtime, and streamline operations. "
        "We focus on empowering workers and enabling smarter decision-making in industrial environments."
    )
    
    discover_competitors(company_description)

    print("\n👥 Extracting engaged users...")
    extract_engaged_users()

    print("\n🧠 Generating outreach messages...")
    generate_outreach_messages()

    print("\n✅ Pipeline completed successfully.")
