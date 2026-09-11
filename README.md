# Jenkins Demo (Pipeline as Code)

Basit bir Flask uygulaması üzerinden Jenkins CI/CD pipeline örneği.
Pipeline tanımı `Jenkinsfile` içinde, kodun yanında Git'te tutulur.

## Pipeline aşamaları
1. **Checkout Bilgisi** – Git'ten çekilen dosyaları listeler
2. **Build Image** – `app/` klasöründen Docker image build eder
3. **Test** – Testleri image içinde çalıştırır (`pytest`)
4. **Deploy (Doğrulama)** – Container'ı ayağa kaldırıp cevap veriyor mu kontrol eder

## Yerelde manuel deneme
```bash
cd app
docker build -t jenkins-demo-app .
docker run -d --name demo -p 5001:5000 jenkins-demo-app
curl http://localhost:5001/
docker rm -f demo
```

## Jenkins'te kurulum
1. New Item → Pipeline
2. Pipeline → Definition: **Pipeline script from SCM**
3. SCM: Git, repo URL'i gir
4. Script Path: `Jenkinsfile`
5. Save → Build Now