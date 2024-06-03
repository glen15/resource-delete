import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_wsu_resume_codebuild_projects():
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodeBuild 클라이언트 생성
    codebuild = session.client('codebuild')
    
    # 프로젝트 목록 가져오기
    response = codebuild.list_projects()
    
    print("START")
    # 이름에 "wsu-resume"가 포함된 프로젝트 찾기
    for project_name in response.get('projects', []):
        if keyword in project_name.lower():  # 소문자로 변환하여 비교
            print(f"\n\n\nFound CodeBuild Project: {project_name}")
            confirmation = input(f"\n\n\nDo you want to delete CodeBuild Project '{project_name}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\n\nDeleting CodeBuild Project: {project_name}")
                codebuild.delete_project(name=project_name)
    print("\n\n\nEND")

if __name__ == '__main__':
    delete_wsu_resume_codebuild_projects(keyword)
