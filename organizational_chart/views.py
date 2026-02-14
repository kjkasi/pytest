from django.shortcuts import render
from django.http import JsonResponse
from .models import OrganizationalChart


def organizational_chart_view(request):
    """
    Отображение организационной диаграммы
    """
    # Получаем корневые элементы (без родителей)
    root_nodes = OrganizationalChart.objects.filter(parent=None)
    
    def build_tree(node):
        """Рекурсивно строим дерево"""
        children = node.children.all()
        tree_node = {
            'id': node.id,
            'name': node.name,
            'description': node.description,
            'level': node.level,
            'children': [build_tree(child) for child in children]
        }
        return tree_node
    
    tree_data = [build_tree(root) for root in root_nodes]
    
    context = {
        'tree_data': tree_data
    }
    return render(request, 'organizational_chart/chart.html', context)


def organizational_chart_json(request):
    """
    Возвращает JSON-представление организационной диаграммы
    """
    root_nodes = OrganizationalChart.objects.filter(parent=None)
    
    def build_tree(node):
        """Рекурсивно строим дерево"""
        children = node.children.all()
        tree_node = {
            'id': node.id,
            'name': node.name,
            'description': node.description,
            'level': node.level,
            'children': [build_tree(child) for child in children]
        }
        return tree_node
    
    tree_data = [build_tree(root) for root in root_nodes]
    
    return JsonResponse(tree_data, safe=False)
