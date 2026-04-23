from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Movie
from .serializer import MovieSerializer


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    """电影视图集"""
    # 定义数据查询集
    queryset = Movie.objects.all()
    # 指定序列化器
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        """获取电影列表"""
        try:
            #获取查询集
            queryset = self.get_queryset()
            # 创建序列化器
            serializer = self.get_serializer(queryset,many=True)
            
            return Response({
                "code":200,
                "message":"获取电影列表成功",
                "total":queryset.count(),
                "data":serializer.data
            },status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "code":500,
                "message":f"获取电影列表失败：{str(e)}",
                "data":None
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)