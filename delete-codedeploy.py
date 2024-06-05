import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_codedeploy_applications(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodeDeploy 클라이언트 생성
    codedeploy = session.client('codedeploy')
    
    # CodeDeploy 애플리케이션 목록 가져오기
    response = codedeploy.list_applications()
    
    print("시작\n\n\n")
    # 이름에 키워드가 포함된 애플리케이션 찾기
    applications_to_delete = [app for app in response.get('applications', []) if keyword in app.lower()]
    
    if applications_to_delete:
        print("찾은 CodeDeploy 애플리케이션 목록:")
        for app_name in applications_to_delete:
            print(f"- {app_name}")
        
        confirmation = input("이 모든 CodeDeploy 애플리케이션을 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirmation == 'y':
            for app_name in applications_to_delete:
                print(f"\n\nCodeDeploy 애플리케이션 삭제 중: {app_name}")
                codedeploy.delete_application(applicationName=app_name)
        else:
            for app_name in applications_to_delete:
                confirmation = input(f"CodeDeploy 애플리케이션 '{app_name}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
                if confirmation == 'y':
                    print(f"\n\nCodeDeploy 애플리케이션 삭제 중: {app_name}")
                    codedeploy.delete_application(applicationName=app_name)
    else:
        print("지정된 키워드가 포함된 애플리케이션을 찾을 수 없습니다.")
    
    print("\n\n\n종료")

if __name__ == '__main__':
    delete_codedeploy_applications(keyword)
