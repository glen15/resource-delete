import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_wsu_resume_codepipelines(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodePipeline 클라이언트 생성
    codepipeline = session.client('codepipeline')
    
    # 파이프라인 목록 가져오기
    response = codepipeline.list_pipelines()
    
    print("START")
    # 이름에 "wsu-resume"가 포함된 파이프라인 찾기
    for pipeline in response.get('pipelines', []):
        if keyword in pipeline['name'].lower():  # 소문자로 변환하여 비교
            print(f"\n\n\nFound Pipeline: {pipeline['name']}")
            confirmation = input(f"\n\n\nDo you want to delete CodePipeline '{pipeline['name']}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\n\nDeleting Pipeline: {pipeline['name']}")
                codepipeline.delete_pipeline(name=pipeline['name'])
    print("\n\n\nEND")

if __name__ == '__main__':
    delete_wsu_resume_codepipelines(keyword)
