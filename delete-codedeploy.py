import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_wsu_resume_codedeploy_applications(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodeDeploy 클라이언트 생성
    codedeploy = session.client('codedeploy')
    
    # 애플리케이션 목록 가져오기
    response = codedeploy.list_applications()
    
    keyword = "wsu-resume"
    
    print("START")
    # 이름에 "wsu-resume"가 포함된 애플리케이션 찾기
    for application_name in response.get('applications', []):
        if keyword in application_name.lower():  # 소문자로 변환하여 비교
            print(f"\n\n\nFound CodeDeploy Application: {application_name}")
            confirmation = input(f"\n\n\nDo you want to delete CodeDeploy Application '{application_name}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\n\nDeleting CodeDeploy Application: {application_name}")
                codedeploy.delete_application(applicationName=application_name)
    print("END")

if __name__ == '__main__':
    delete_wsu_resume_codedeploy_applications(keyword)
