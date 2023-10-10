// const data = {
//     "id": 1,
//     "productName": "버그를 Java라 버그잡는 개리씨 키링 개발자키링 금속키링",
//     "price": 12500,
//     "stockCount": 100,
//     "thumbnailImg": "asset/img/1/thumbnailImg.jpg",
//     "option": [],
//     "discountRate": 0,
//     "shippingFee": 1500,
//     "detailInfoImage": [
//     "asset/detail/2/detail1.png",
//     "asset/detail/2/detail2.png"
//     ],
//     "viewCount": 0,
//     "pubDate": "2022-02-28",
//     "modDate": "2022-02-28"
// }

const BASE_URL = "http://test.api.weniv.co.kr/"
const mainContainer = document.getElementById("main");


// 상품 카드 만드는 부분
// 상품 이미지 주소, 가격, 상품이름을 받으면 상품 카드를 만들어주는 함수
function createProductCard(imgUrl, price, productName, onClick){
    // $productCard = elementproductCard
    const $productCard = document.createElement("div");
    const $productName = document.createElement("strong");
    const $price = document.createElement("span");
    // const $thumbnailImg = document.createElement("img");

    // $thumbnailImg.src = imgUrl;
    $price.innerText = price + "원";
    $productName.innerText = productName;
    // $productCard.append($thumbnailImg, $productName, $price);
    $productCard.append($productName, $price);
    $productCard.addEventListener("click",onClick);  //이벤트

    return $productCard
}

function createProductDetail(imgUrl){
    const $ProductDetail = document.createElement("img");
    $ProductDetail.src = imgUrl;
    return $ProductDetail
}

// --------------------------------------------------------
function main(){

    const productContainer = document.createElement("div");
    productContainer.id = "product";
    const detailContainer = document.createElement("div");
    detailContainer.id = "detail";
    mainContainer.appendChild(productContainer);
    mainContainer.appendChild(detailContainer);
    fetch(BASE_URL+"mall").then((res)=>{
        return res.json();
    }).then((json)=>{
        console.log(json);
        json.forEach(data=>{
            const productId = data.id;
            const productImgUrl = BASE_URL+data.thumbnailImg;
            const productName = data.productName;
            const price = data.price;
            console.log(data);
            const onClick = async (e)=>{
                detailContainer.innerHTML = ""
                // console.log(productId,"번 상품 클릭");
                const res = await fetch(BASE_URL+"mall/"+productId);
                const json =await res.json();
                json.detailInfoImage.forEach(imgUrl=>{
                    const detailImgUrl = BASE_URL+imgUrl
                    const $ProductDetail = createProductDetail(detailImgUrl)
                    detailContainer.appendChild($ProductDetail);
                })
                // console.log(json);
            }
            
            const $productCard = createProductCard(productImgUrl,price,productName,onClick)
            productContainer.appendChild($productCard);
        })
    });
    
    
    
}

main();
