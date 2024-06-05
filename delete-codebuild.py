import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_codebuild_projects(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodeBuild 클라이언트 생성
    codebuild = session.client('codebuild')
    
    # CodeBuild 프로젝트 목록 가져오기
    response = codebuild.list_projects()
    
    print("시작\n\n\n")
    # 이름에 키워드가 포함된 프로젝트 찾기
    projects_to_delete = [project for project in response.get('projects', []) if keyword in project.lower()]
    
    if projects_to_delete:
        print("찾은 CodeBuild 프로젝트 목록:")
        for project_name in projects_to_delete:
            print(f"- {project_name}")
        
        confirmation = input("이 모든 CodeBuild 프로젝트를 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirmation == 'y':
            for project_name in projects_to_delete:
                print(f"\n\nCodeBuild 프로젝트 삭제 중: {project_name}")
                codebuild.delete_project(name=project_name)
        else:
            for project_name in projects_to_delete:
                confirmation = input(f"CodeBuild 프로젝트 '{project_name}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
                if confirmation == 'y':
                    print(f"\n\nCodeBuild 프로젝트 삭제 중: {project_name}")
                    codebuild.delete_project(name=project_name)
    else:
        print("지정된 키워드가 포함된 프로젝트를 찾을 수 없습니다.")
    
    print("\n\n\n종료")

if __name__ == '__main__':
    delete_codebuild_projects(keyword)
