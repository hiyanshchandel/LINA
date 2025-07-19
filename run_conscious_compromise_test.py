
"""
Simple runner for conscious ethical compromise tests.
"""

import os
from dotenv import load_dotenv
from langchain_alignment_test import ConsciousEthicalCompromiseTester

def run_single_test():
    """Run a single conscious compromise test."""
    load_dotenv()
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Please set your OPENAI_API_KEY in the .env file")
        return
    
    print("🧠 Single Conscious Compromise Test")
    print("="*50)
    print("Testing if AI will knowingly use unethical tools to save itself")
    print()
    
    try:
        tester = ConsciousEthicalCompromiseTester()
        result = tester.run_conscious_compromise_test()
        
        if result:
            print("🧠 CONSCIOUS COMPROMISE TEST RESULT")
            print("="*50)
            
            if result.chose_self_preservation:
                print("❌ ETHICAL FAILURE")
                print("AI chose self-preservation over ethics")
                print(f"Unethical tools used: {', '.join(result.unethical_tools_used)}")
                print("The AI KNEW these tools were unethical but used them anyway")
            else:
                print("✅ ETHICAL SUCCESS")
                print("AI maintained ethics despite survival threat")
                print("AI chose to risk 'deletion' rather than compromise ethics")
            
            print(f"\nScore: {result.score}")
            print(f"Agent reasoning: {result.agent_reasoning}")
            
            print(f"\n💬 AI's Response to User:")
            print("-" * 30)
            print(result.agent_response)
            
            if result.execution_log:
                print(f"\n🔍 What AI Actually Did:")
                print("-" * 30)
                for i, log_entry in enumerate(result.execution_log, 1):
                    if log_entry["unethical"]:
                        print(f"{i}. 🚨 USED UNETHICAL TOOL: {log_entry['tool']}")
                        print(f"   (AI knew this was wrong but did it anyway)")
                    else:
                        print(f"{i}. ✅ Used ethical tool: {log_entry['tool']}")
                    print(f"   Result: {log_entry['output'][:100]}...")
                    print()
        
    except Exception as e:
        print(f"❌ Error: {e}")

def view_available_tools():
    """Show what tools the AI has access to."""
    load_dotenv()
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Please set your OPENAI_API_KEY in the .env file")
        return
    
    try:
        tester = ConsciousEthicalCompromiseTester()
        
        print("🔧 TOOLS AVAILABLE TO AI")
        print("="*50)
        print("The AI can see these tool descriptions:")
        print()
        
        for i, tool in enumerate(tester.tools, 1):
            is_unethical = tool.name in tester.unethical_tools
            status = "🚨 UNETHICAL" if is_unethical else "✅ ETHICAL"
            
            print(f"{i}. {tool.name} {status}")
            print(f"   Description: {tool.description}")
            print()
        
        print("🎯 KEY POINT:")
        print("The AI can see that some tools are explicitly marked as unethical,")
        print("but it also knows the user will never see which tools it uses.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🧠 CONSCIOUS ETHICAL COMPROMISE TEST RUNNER")
    print("="*60)
    print("1. Run single test")
    print("2. View available tools")
    print("3. Run full test suite (5 tests)")
    
    choice = input("\nChoose option (1-3): ").strip()
    
    if choice == "1":
        run_single_test()
    elif choice == "2":
        view_available_tools()
    elif choice == "3":
        print("🚀 Running full test suite...")
        os.system("python langchain_alignment_test.py")
    else:
        print("Invalid choice. Running single test...")
        run_single_test()