from pydantic import BaseModel
from datetime import datetime, timedelta

# fastapi
from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse

from zzm import model_jiwon,model1, model2, model3,model4,model5,model6
# from nltk.tokenize import word_tokenize


routes = APIRouter(prefix="/api")

# @router.post('/prediction/cvl_corp_sentences')
# async def cvl_corp_sentences(req_corp_sentence) :
#     test_data = word_tokenize("삼성전자는 반도체의성능과 생산성을 높이기 위해 그 크기를 줄이는 데 목적을 두고 있습니다. 현재 반도체 공정의 크기는 EUV장비 도입으로 7나노공정까지 양산할 수 있으며 이후에는 5나노, 3나노 공정개발에 노력을 기울이고 있습니다. 이번 Foundry사업부 직무 체험의 장에 참여하며 반도체 공정기술에대한 정확한 직무에 대해 파악했으며 향후 시스템 반도체의 성장 가능성에 대해 알게 되었습니다. 저는삼성전자 Foundry사업부에 입사한 후 7나노공정과 함께회사가 지금보다도 성장할 수 있도록 힘쓰고 싶고 더 나아가 전 세계 Foundry시장을 선도할 수 있도록노력할 것입니다.  최근 사회이슈 중 중요하다고 생각되는 한가지를 선택하고 이에 관한 자신의 견해를 기술해 주시기 바랍니다.[수소연료전지와반도체의 관계] 제가 최근 중요하게 생각하는 사회이슈는 신재생에너지 중 수소연료전지입니다. 현재 대한민국의 가장 큰 문제라고 생각하면 많은 사람이 미세먼지 또는 지구온난화라고 말할 것입니다. 한국은 더 이상 마스크 없이는 살아갈 수 없게 되었습니다. 우리가많이 사용하고 있는 석탄, 석유, 천연가스등의 화석연료는전체 에너지의 가장 많은 비율을 차지하고 있으며 지구 온난화와 기후변화 또는 미세먼지 같은 환경적인 문제를 야기하고 있습니다. 그래서 전 세계에서는 화석연료의 고갈과 환경문제를 생각하여 새로운 에너지인 신재생에너지를 개발하고 있습니다. 그중에서 저는 수소연료전지에 대해 큰 관심을 가지고 있습니다. 수소연료전지는수소를 이용한 전기에너지를 생산해 내는 전지이며 많은 대체에너지가 개발되고 있지만 향후에 가장 큰 효율을 낼 수 있고 친환경적인 에너지라고 생각합니다. 수소와 산소의 산화 환원 반응에 의해 전기가 생성되며 생성물로는 물로서 유해 배출가스가 거의 없다고 볼 수있습니다.  연료전지는 아직도 상용화를 위해 많은 연구가 필요한 것으로 나타나 있습니다. 특히 한국은 미국과 일본에 비교하면 수소연료전지 부분에서 많이 뒤처져 있습니다. 최근 연구 중에는 연료전지 내부에서 전력변환장치 성능을 향상하는 중요한 요소 중 스위칭 소자를 개선하는 기술개발이이루어지고 있습니다. 그 스위칭 소자에는 금속산화막 전계효과트랜지스터로 활용 가능한 갈륨질화물 반도체가사용될 수 있고 전력변환 시 발생하는 손실을 줄일 수 있습니다. 또한,서울과기대 안지환 교수팀은 고체산화물 연료전지에 ALD 반도체 증착공정 기술을 적용하여기존 저온형 고체산화물 연료전지의 성능이 낮아진다는 단점을 극복할 수 있었습니다. 이처럼 저는 미래의 에너지에서 수소연료전지의 중요성을 느끼고 있고 연료전지와 함께 반도체 소자와공정 기술의 필요성 또한 느끼고 있습니다. 반도체 소자는 미래에 어느 분야에도 끊임없이 쓰일 것으로생각합니다.지원 직무에 대해 본인이 이해한 내용을 서술하고, 본인이 해당 직무에 적합한 사유를 전공능력 측면에서 구체적으로 서술하시오. 제가 지원한 Foundry사업부의 공정기술직무는 반도체 공정기술을 개발하고 안정적인 수율과 높은 품질의 제품을 위한 최상의 솔루션을 제공하는 것으로 알고 있습니다. 이번 Foundry직무 체험의 장에서 현업에 계신 선배님과의 대화를통해 eFlash, CIS, DDI와 같은 비메모리 반도체의 기술개발과 반도체 수율 향상을 위한 노력을하고 있다고 배웠습니다. 저는 반도체 소자라는 수업을 들으면서 전반적으로 MOSFET과Inverter의 동작원리와 구조에 관해 공부를 하였으며channel이 형성되었을 때의 전기적 특성과 defect에 따른 변화에 관해 공부를 하였습니다. 또한, 반도체 공정과 나노소재개론 수업에서 반도체 산업과 8대 공정에 대한 강의를 이수했으며 클린룸에 들어가 실험할 수 있는 기회가 있었습니다. 반도체 증착 공정에서 ALD증착으로 만든 Metal-Insulator-Metal소자의 전기적 특성측정을 해보았으며 이 실험에서 주파수와 커패시턴스에 따라유전체의 유전률을 구할 수 있었습니다.".lower())
#     result = model.docvecs.most_similar(positive=[model.infer_vector(test_data)],negative=['자료없음'],topn=5)
#     return JSONResponse({'result': result})

class Request_by(BaseModel):
    corp_nm : str


@routes.get('/bye/')
async def bye():
    return{"byy":"vbb"}


# @routers.post('/prediction/cvl_corp_nm')
# async def cvl_corp_nm(request: Request_by) : 
#     results = {}

#     """지원항목이 비슷한 기업을 찾아준다"""
#     results['similar_doc_jiwon'] = model_jiwon.docvecs.most_similar(request.corp_nm,topn=5)
#     """경험항목이 비슷한 기업들"""
#     results['similar_doc_exp'] = model1.docvecs.most_similar(request.corp_nm,topn=5)
#     """자소서 작성시 성장과정이 유사한 기업들 """
#     results['similar_doc_grow'] = model2.docvecs.most_similar(request.corp_nm,topn=5)
#     """자소서 작성시 직무 유사한 기업들 """
#     results['similar_doc_duty'] = model3.docvecs.most_similar(request.corp_nm,topn=5)
#     """자소서 작성시 성격 장단점이 유사한 기업들 """
#     results['similar_doc_cha'] = model4.docvecs.most_similar(request.corp_nm,topn=5)
#     """자소서 작성시 이슈가 유사한 기업들 """
#     results['similar_doc_iss'] = model5.docvecs.most_similar(request.corp_nm,topn=5)
#     """자소서 작성시 기타 란이 유사한 기업들 """
#     results['similar_doc_etc'] = model6.docvecs.most_similar(request.corp_nm,topn=5)

#     return JSONResponse(results, status_code=200)
