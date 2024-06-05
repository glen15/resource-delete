import boto3

### 지워야하는 리소스 키워드 ###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name = 'TARGET REGION'

def delete_code_pipelines(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # CodePipeline 클라이언트 생성
    codepipeline = session.client('codepipeline')
    
    # CodePipeline 목록 가져오기
    response = codepipeline.list_pipelines()
    
    print("시작\n\n\n")
    # 이름에 키워드가 포함된 파이프라인 찾기
    pipelines_to_delete = [pipeline['name'] for pipeline in response.get('pipelines', []) if keyword in pipeline['name'].lower()]
    
    if pipelines_to_delete:
        print("찾은 CodePipeline 목록:")
        for pipeline_name in pipelines_to_delete:
            print(f"- {pipeline_name}")
        
        confirmation = input("이 모든 CodePipeline을 삭제하시겠습니까? (y/n): ").strip().lower()
        if confirmation == 'y':
            for pipeline_name in pipelines_to_delete:
                print(f"\n\nCodePipeline 삭제 중: {pipeline_name}")
                codepipeline.delete_pipeline(name=pipeline_name)
        else:
            for pipeline_name in pipelines_to_delete:
                confirmation = input(f"CodePipeline '{pipeline_name}'을(를) 삭제하시겠습니까? (y/n): ").strip().lower()
                if confirmation == 'y':
                    print(f"\n\nCodePipeline 삭제 중: {pipeline_name}")
                    codepipeline.delete_pipeline(name=pipeline_name)
    else:
        print("지정된 키워드가 포함된 파이프라인을 찾을 수 없습니다.")
    
    print("\n\n\n종료")

if __name__ == '__main__':
    delete_code_pipelines(keyword)
