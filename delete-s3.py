import boto3
### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

###
def delete_s3_buckets(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # S3 클라이언트 생성
    s3 = session.client('s3')
    s3_resource = session.resource('s3')
    
    # 버킷 목록 가져오기
    response = s3.list_buckets()
    
    print("START\n\n\n")
    # 이름에 키워드가 포함된 버킷 찾기
    for bucket in response.get('Buckets', []):
        bucket_name = bucket['Name']
        if keyword in bucket_name.lower():  # 소문자로 변환하여 비교
            print(f"Found S3 Bucket: {bucket_name}")
            confirmation = input(f"Do you want to delete S3 Bucket '{bucket_name}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\nDeleting all objects in S3 Bucket: {bucket_name}")
                # 버킷 비우기
                bucket_resource = s3_resource.Bucket(bucket_name)
                bucket_resource.objects.delete()
                
                # 버킷 버전이 활성화된 경우 모든 버전 삭제
                bucket_versioned = s3_resource.Bucket(bucket_name)
                bucket_versioned.object_versions.delete()
                
                print(f"\n\nDeleting S3 Bucket: {bucket_name}")
                s3.delete_bucket(Bucket=bucket_name)
    print("\n\n\nEND")

if __name__ == '__main__':
    delete_s3_buckets(keyword)
