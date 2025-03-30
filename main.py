from agent import PersonalInfoLawAgent

if __name__ == "__main__":
    agent = PersonalInfoLawAgent()
    
    # 실행 예제
    inputs = {"question": "개인정보 처리에 대한 동의를 받을 때 주의해야 할 점은 무엇인가요?"}
    for output in agent.run(inputs):
        for key, value in output.items():
            print(f"Node '{key}':")
            print(f"Value: {value}\n")
        print("\n----------------------------------------------------------\n")