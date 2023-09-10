docker build -t docker push rookblack/ocr_donor:redis -f Dockerfile.redis ../
docker build -t docker push rookblack/ocr_donor:web -f Dockerfile.web ../
docker build -t docker push rookblack/ocr_donor:worker -f Dockerfile.worker ../
docker compose up